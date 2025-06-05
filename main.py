from data_loader import load_data
from llm_client import summarize_text
from output_writer import write_output
import os

DATA_DIR = 'Data'
OUTPUT_DIR = 'output'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'summary.txt')

if __name__ == '__main__':
    # Load data
    data = load_data(DATA_DIR)
    
    # Summarize data using LLM
    summary = summarize_text(data)
     
    # Write output to file
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_output(OUTPUT_FILE, data, summary)
    print(f"Summary written to {OUTPUT_FILE}") 