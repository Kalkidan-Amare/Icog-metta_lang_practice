# Metta-LLM Integration

This project extends Metta to enable it to:
- Call a Large Language Model (LLM) to summarize information from data files.
- Make modifications to a space (data or knowledge base).
- Write output to a file in a human-readable fashion.

## Features
- Uses data from the [Rejuve Annotation Query Backend Data](https://github.com/rejuve-bio/annotation-query-backend/tree/main/Data).
- Sends relevant data to an LLM for summarization.
- Saves the summary and relevant information in Metta.
- Outputs results to a human-readable file.

## Usage
1.  Place data files from the Rejuve Annotation Query Backend `Data` directory into the local `Data/` directory.
2.  Run the main script to process the data, call the LLM, and save the results.
3.  The output will be written to `output/summary.txt`.

## Requirements
- Python 3.8+
- OpenAI API key (or compatible LLM API)
- See `requirements.txt` for dependencies.

## Project Structure
- `main.py` - Entry point for the integration
- `llm_client.py` - Handles LLM API calls
- `data_loader.py` - Loads and preprocesses data
- `output_writer.py` - Writes human-readable output
- `Data/` - Place input data files here
- `output/` - Output directory for results

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## License
MIT