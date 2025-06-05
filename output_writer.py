def write_output(filepath: str, data: str, summary: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=== Original Data ===\n")
        f.write(data[:2000] + ('...\n\n' if len(data) > 2000 else '\n\n'))
        f.write("=== LLM Summary ===\n")
        f.write(summary + '\n\n')