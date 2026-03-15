# Push para GitHub - Instruções

## Autor
**Rui Lima** - PUC Minas

## Repositório
https://github.com/Quanticoi/bakta-local

## Como fazer o Push

### Opção 1: Usando Token de Acesso Pessoal (Recomendado)

1. Gere um token em: https://github.com/settings/tokens
2. Execute:
```bash
git push https://SEU_TOKEN@github.com/Quanticoi/bakta-local.git main --force
```

### Opção 2: Usando GitHub CLI

```bash
gh auth login
git push -u origin main --force
```

### Opção 3: Usando SSH

```bash
# Configure sua chave SSH primeiro
git remote set-url origin git@github.com:Quanticoi/bakta-local.git
git push -u origin main --force
```

## Status do Commit

✅ Commit criado localmente com sucesso!
- **Hash:** 0ed7e0d
- **Mensagem:** PUC Minas - Bakta: Plataforma de Anotacao Genomica
- **Autor:** Rui Lima
- **Arquivos:** 45 arquivos, ~11.000 linhas de código

## Conteúdo do Commit

### Estrutura
```
Bakta/
├── backend/          # API Flask + Pipeline
├── frontend/         # Interface web
├── deployment/       # Docker
├── docs/             # Documentação
├── tests/            # Testes
├── data/             # Templates
└── assets/           # Imagens
```

### Funcionalidades
- ✅ Upload de genomas FASTA
- ✅ Anotação com Bakta
- ✅ Visualização de resultados
- ✅ API REST completa
- ✅ Docker containerization
- ✅ Testes automatizados

## Nota

Projeto desenvolvido por **Rui Lima** como parte das atividades acadêmicas da PUC Minas.
