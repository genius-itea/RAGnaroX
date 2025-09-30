import os
import json
import glob
import argparse


def calculate_metrics(retrieved_lists, gold_lists):
    hits_at_4_count = 0
    map_at_4_list = []
    mrr_list = []

    for retrieved, gold in zip(retrieved_lists, gold_lists):
        hits_at_4_flag = False
        first_relevant_rank = None

        # Clean gold and retrieved texts
        gold_clean = [item.replace(" ", "").replace("\n", "").lower() for item in gold]
        retrieved_clean = [item.replace(" ", "").replace("\n", "").lower() for item in retrieved]

        # Find all relevant positions (documents that contain the gold answer)
        relevant_positions = []

        for rank, retrieved_item in enumerate(retrieved_clean[:4], start=1):
            is_relevant = any(gold_item in retrieved_item for gold_item in gold_clean)
            if is_relevant:
                relevant_positions.append(rank)
                if first_relevant_rank is None:
                    first_relevant_rank = rank
                hits_at_4_flag = True

        # Calculate Hits@4
        hits_at_4_count += int(hits_at_4_flag)

        # Calculate MRR@4 (reciprocal of first relevant rank)
        mrr_list.append(1 / first_relevant_rank if first_relevant_rank else 0)

        # Calculate MAP@4 (average precision for this query)
        # For single gold answer case: AP = sum of (relevant_docs_up_to_rank_i / rank_i) / total_relevant_docs_in_collection
        if relevant_positions:
            precision_sum = 0
            for i, rank in enumerate(relevant_positions):
                precision_at_rank = (i + 1) / rank  # (i+1) relevant docs found up to this rank
                precision_sum += precision_at_rank

            # Average precision = sum of precisions at relevant positions / number of relevant docs in collection
            # For our case, we treat each match as finding the same relevant document
            # So we divide by the number of relevant documents in the gold standard (always 1)
            average_precision = precision_sum / len(relevant_positions)  # Normalize by actual relevant docs found
        else:
            average_precision = 0

        map_at_4_list.append(average_precision)

    # Calculate average metrics over all queries
    hits_at_4 = hits_at_4_count / len(gold_lists)
    map_at_4 = sum(map_at_4_list) / len(gold_lists)
    mrr_at_4 = sum(mrr_list) / len(gold_lists)

    return {
        'Hits@4': hits_at_4,
        'MAP@4': map_at_4,
        'MRR@4': mrr_at_4,
    }


def main_eval(file_name):
    print(f'For file: {file_name}')
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        print(f'Loaded {len(data)} entries from file')
    except Exception as e:
        print(f'Error loading file: {e}')
        return

    retrieved_lists = []
    gold_lists  = []

    for i, d in enumerate(data):
        # Skip entries without retrieved contexts or reference
        if 'retrieved_contexts' not in d or 'reference' not in d:
            print(f'Skipping entry {i}: missing required fields')
            continue

        # Extract retrieved contexts and reference answer
        retrieved_lists.append(d['retrieved_contexts'])
        gold_lists.append([d['reference']])

    print(f'Processing {len(retrieved_lists)} valid entries')

    if len(retrieved_lists) == 0:
        print('No valid entries found!')
        return

    # Calculate metrics
    metrics = calculate_metrics(retrieved_lists, gold_lists)

    # Print the metrics
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    print('-'*20)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Evaluation script with a file parameter.")
    parser.add_argument('--file', type=str, required=False, help='File Name')
    parser.add_argument('--path', type=str, required=False, default="results", help='Folder Path')
    args = parser.parse_args()

    if args.file:
        print(f"Evaluate file: {args.file}")
        main_eval(args.file)
    else:
        path = args.path
        json_files = glob.glob(os.path.join(path, '*multi_qwen4B_multi*.json'))
        print(f"Evaluate multi_qwen14B_multi files in folder: {path}")
        for file in json_files:
            main_eval(file)

# Example: python3 0_multi-hop-rag-evaluation-extended.py --file 10-doc-multi_qwen4B_multi5_bge.json
