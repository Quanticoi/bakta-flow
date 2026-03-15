#!/usr/bin/env python3
"""
PUC Minas - Download Templates NCBI
Script para baixar templates de genomas do NCBI
"""

import os
import sys
import requests
import argparse
from pathlib import Path
from urllib.parse import urlencode

# Configurações
NCBI_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
NCBI_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
NCBI_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Templates pré-definidos
TEMPLATES = {
    "ecoli_k12": {
        "name": "Escherichia coli K-12",
        "accession": "NC_000913.3",
        "description": "Genoma de referência de E. coli K-12"
    },
    "ecoli_puc19": {
        "name": "E. coli plasmid pUC19",
        "accession": "L09137.1",
        "description": "Plasmídeo pUC19 (vetor de clonagem)"
    },
    "bsubtilis": {
        "name": "Bacillus subtilis 168",
        "accession": "NC_000964.3",
        "description": "Genoma de referência de B. subtilis"
    },
    "saureus": {
        "name": "Staphylococcus aureus",
        "accession": "NC_007795.1",
        "description": "Genoma de S. aureus NCTC 8325"
    },
    "pseudomonas": {
        "name": "Pseudomonas aeruginosa",
        "accession": "NC_002516.2",
        "description": "Genoma de P. aeruginosa PAO1"
    },
    "salmonella": {
        "name": "Salmonella enterica",
        "accession": "NC_003198.1",
        "description": "Genoma de S. enterica Typhimurium"
    }
}


def download_from_ncbi(accession: str, output_path: Path, db: str = "nucleotide", rettype: str = "fasta") -> bool:
    """
    Download de sequência do NCBI.
    
    Args:
        accession: Número de acesso NCBI
        output_path: Caminho para salvar o arquivo
        db: Banco de dados NCBI
        rettype: Tipo de retorno
        
    Returns:
        True se sucesso, False caso contrário
    """
    print(f"  Baixando {accession}...", end=" ")
    
    params = {
        "db": db,
        "id": accession,
        "rettype": rettype,
        "retmode": "text"
    }
    
    try:
        response = requests.get(NCBI_EFETCH, params=params, timeout=60)
        response.raise_for_status()
        
        # Verificar se conteúdo é válido
        content = response.text.strip()
        if not content.startswith(">"):
            print("❌ (conteúdo inválido)")
            return False
        
        # Salvar arquivo
        output_path.write_text(content)
        print(f"✅ ({len(content)} bytes)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ (erro: {e})")
        return False


def create_dummy_template(output_path: Path, name: str, size: int = 5000) -> bool:
    """
    Cria um template FASTA dummy para testes.
    
    Args:
        output_path: Caminho para salvar
        name: Nome da sequência
        size: Tamanho em bp
        
    Returns:
        True se sucesso
    """
    import random
    
    print(f"  Criando template dummy: {name}...", end=" ")
    
    # Gerar sequência aleatória
    bases = ['A', 'T', 'G', 'C']
    sequence = ''.join(random.choices(bases, k=size))
    
    # Formatar em linhas de 60 caracteres
    lines = [sequence[i:i+60] for i in range(0, len(sequence), 60)]
    
    fasta_content = f">{name} synthetic genome for testing\n" + "\n".join(lines)
    
    output_path.write_text(fasta_content)
    print(f"✅ ({size} bp)")
    return True


def download_all_templates(output_dir: Path, use_dummy: bool = False) -> dict:
    """
    Baixa todos os templates definidos.
    
    Args:
        output_dir: Diretório de saída
        use_dummy: Se True, cria templates dummy em vez de baixar do NCBI
        
    Returns:
        Dicionário com resultados
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = {
        "success": [],
        "failed": []
    }
    
    print(f"\n📁 Diretório de templates: {output_dir}")
    print("=" * 60)
    
    for template_id, info in TEMPLATES.items():
        print(f"\n🔬 {info['name']}")
        print(f"   {info['description']}")
        
        output_file = output_dir / f"{template_id}.fasta"
        
        if use_dummy:
            success = create_dummy_template(output_file, info['name'])
        else:
            success = download_from_ncbi(info['accession'], output_file)
        
        if success:
            results["success"].append({
                "id": template_id,
                "name": info['name'],
                "file": str(output_file)
            })
        else:
            results["failed"].append(template_id)
    
    return results


def list_templates(output_dir: Path):
    """Lista templates disponíveis."""
    print("\n📋 Templates disponíveis:")
    print("=" * 60)
    
    for template_id, info in TEMPLATES.items():
        print(f"\n  {template_id}")
        print(f"    Nome: {info['name']}")
        print(f"    Acesso: {info['accession']}")
        print(f"    Descrição: {info['description']}")
        
        # Verificar se existe
        output_file = output_dir / f"{template_id}.fasta"
        if output_file.exists():
            size = output_file.stat().st_size
            print(f"    Status: ✅ Baixado ({size:,} bytes)")
        else:
            print(f"    Status: ❌ Não baixado")


def main():
    parser = argparse.ArgumentParser(
        description="Download de templates de genomas do NCBI"
    )
    parser.add_argument(
        "--output",
        default="./templates",
        help="Diretório de saída para templates"
    )
    parser.add_argument(
        "--dummy",
        action="store_true",
        help="Criar templates dummy em vez de baixar do NCBI"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Listar templates disponíveis"
    )
    
    args = parser.parse_args()
    output_dir = Path(args.output)
    
    print("=" * 60)
    print("  PUC Minas - Download de Templates NCBI")
    print("=" * 60)
    
    if args.list:
        list_templates(output_dir)
        return
    
    # Download
    results = download_all_templates(output_dir, use_dummy=args.dummy)
    
    # Resumo
    print("\n" + "=" * 60)
    print("  RESUMO")
    print("=" * 60)
    print(f"✅ Sucesso: {len(results['success'])}")
    print(f"❌ Falhas: {len(results['failed'])}")
    
    if results['success']:
        print("\nTemplates baixados:")
        for item in results['success']:
            print(f"  - {item['name']}")
    
    if results['failed']:
        print("\nTemplates com falha:")
        for item in results['failed']:
            print(f"  - {item}")
    
    # Código de saída
    sys.exit(0 if len(results['success']) > 0 else 1)


if __name__ == "__main__":
    main()
