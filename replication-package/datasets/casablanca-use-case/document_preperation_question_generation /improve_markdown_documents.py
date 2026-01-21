import os
import re
import logging
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def remove_navigation_header(content: str) -> str:
    """
    Removes content between '[Zum Hauptinhalt springen]' and 'Auf dieser Seite'.
    """
    pattern = r"\[Zum Hauptinhalt springen\].*?Auf dieser Seite"
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)
    return cleaned_content

def reformat_with_ai_linting(content: str) -> str:
    """
    Takes input text and returns a valid, well-formatted Markdown version
    without changing the content meaning.
    """
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": (
                "You are a Markdown formatter. Ensure the text is valid Markdown and well structured! "
                "Do not alter the meaning of the content.\n\n"
                "Consider also: \n"
                "- Use `*` for lists.\n"
                "- Add line breaks where necessary for better readability.\n"
                "- If there is code, wrap it in fenced blocks with the correct language tag (e.g., ```python).\n"
                "- Convert keywords like 'Info', 'Wichtig', etc. into headings (## ...).\n"
                "- Check that links and images are correctly formatted and fix them if needed.\n"
                "- Headings should be surrounded by blank lines."
                "- Multiple headings cannot contain the same content."
                "- Each file should end with a single newline character. "
            )},
            {"role": "user", "content": content}
        ],
    )

    return response.choices[0].message.content.strip()


def process_document(input_path: str, output_path: str) -> None:
    """
    Process a single document by removing navigation headers and reformatting with AI.
    """
    try:
        # Read content from input file
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Apply processing functions
        cleaned_content = remove_navigation_header(content)
        reformatted_content = reformat_with_ai_linting(cleaned_content)

        # Write processed content to output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(reformatted_content)

        logging.info(f"Successfully processed: {os.path.basename(input_path)}")
    except Exception as e:
        logging.error(f"Error processing {input_path}: {str(e)}")


def process_all_documents():
    """
    Process all documents in the documents folder and save results to documents-improved folder.
    """
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    documents_dir = os.path.join(base_dir, 'documents')
    improved_dir = os.path.join(base_dir, 'documents-improved')

    # Create improved directory if it doesn't exist
    os.makedirs(improved_dir, exist_ok=True)

    # Get list of all markdown files in documents directory
    md_files = [f for f in os.listdir(documents_dir) if f.endswith('.md')]

    logging.info(f"Found {len(md_files)} markdown files to process")

    # Process each file
    for md_file in md_files:
        input_path = os.path.join(documents_dir, md_file)
        output_path = os.path.join(improved_dir, md_file)
        process_document(input_path, output_path)

    logging.info("Document processing complete!")


if __name__ == '__main__':
    load_dotenv()
    process_all_documents()