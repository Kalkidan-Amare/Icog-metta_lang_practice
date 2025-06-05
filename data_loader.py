import os
import re

def parse_metta_file(content: str) -> str:
    # Extract gene information using regex
    gene_pattern = r'\(gene\s+(\S+)\)'
    gene_name_pattern = r'\(gene_name\s+\(gene\s+(\S+)\)\s+(\S+)\)'
    synonyms_pattern = r'\(synonyms\s+\(gene\s+(\S+)\)\s+\((.*?)\)\)'
    
    genes = {}
    
    # Find all genes
    for match in re.finditer(gene_pattern, content):
        gene_id = match.group(1)
        genes[gene_id] = {'id': gene_id}
    
    # Add gene names
    for match in re.finditer(gene_name_pattern, content):
        gene_id, name = match.groups()
        if gene_id in genes:
            genes[gene_id]['name'] = name
    
    # Add synonyms
    for match in re.finditer(synonyms_pattern, content):
        gene_id, synonyms = match.groups()
        if gene_id in genes:
            genes[gene_id]['synonyms'] = synonyms.split()
    
    # Format the data for LLM
    formatted_data = []
    for gene_id, info in genes.items():
        gene_info = f"Gene ID: {gene_id}"
        if 'name' in info:
            gene_info += f"\nName: {info['name']}"
        if 'synonyms' in info:
            gene_info += f"\nSynonyms: {', '.join(info['synonyms'])}"
        formatted_data.append(gene_info)

    print(formatted_data)
    
    return "\n\n".join(formatted_data)

def load_data(data_dir: str) -> str:
    """
    Load and process all data files from the given directory.
    """
    data = []
    if not os.path.exists(data_dir):
        return ""
    
    for fname in os.listdir(data_dir):
        fpath = os.path.join(data_dir, fname)
        if os.path.isfile(fpath) and fname.lower().endswith('.metta'):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                parsed_data = parse_metta_file(content)
                data.append(parsed_data)
    
    return '\n\n'.join(data) 