#!/usr/bin/env python3
"""
Generate synthetic dataset for RAG evaluation using RAGAS framework.
This script processes markdown documents and creates test questions and answers.
"""

import os
import asyncio
import json
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from ragas.testset import TestsetGenerator
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.testset.graph import KnowledgeGraph, Node, NodeType
from ragas.testset.persona import Persona
from ragas.testset.transforms import default_transforms, apply_transforms, HeadlineSplitter
from ragas.testset.synthesizers import default_query_distribution, SingleHopSpecificQuerySynthesizer
from ragas.testset.transforms.extractors import NERExtractor

# Load environment variables from .env file
load_dotenv()

# Check if API key is available in environment
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")

async def main():
    """Load documents, create knowledge graph, and generate synthetic test data."""
    # Load documents
    path = "improved-documents/"
    loader = DirectoryLoader(path, glob="**/*.md")
    docs = loader.load()


    generator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
    generator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

    personas = [
        Persona(
            name="Kunde",
            role_description="Du hast detailierte Fragen von CASABLANCA beantwortet haben.",
        ),
        Persona(
            name="Technischer Support",
            role_description="Du möchtest technische Details fragen.",
        )

    ]

    transforms = [HeadlineSplitter(), NERExtractor()]

    generator = TestsetGenerator(
        llm=generator_llm, embedding_model=generator_embeddings, persona_list=personas
    )

    distribution = [
        (SingleHopSpecificQuerySynthesizer(llm=generator_llm), 1.0),
    ]

    for query, _ in distribution:
        prompts = await query.adapt_prompts("german", llm=generator_llm)
        query.set_prompts(**prompts)

    dataset = generator.generate_with_langchain_docs(
        docs[:],
        testset_size=100,
        transforms=transforms,
        query_distribution=distribution,
    )

    # Save the generated dataset with proper encoding for German characters
    pandas_dataset = dataset.to_pandas()
    print(pandas_dataset)

    # Save with ensure_ascii=False to properly handle umlauts and other special characters
    with open("dataset.json", 'w', encoding='utf-8') as f:
        # Convert pandas DataFrame directly to dict and then to JSON to preserve special characters
        dataset_dict = pandas_dataset.to_dict(orient='records')
        json.dump(dataset_dict, f, ensure_ascii=False)
        # save the dataset as JSON
        print("Dataset saved successfully.")


if __name__ == "__main__":
    # Run the async main function using asyncio
    asyncio.run(main())
