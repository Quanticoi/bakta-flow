#!/bin/bash
# PUC Minas - Bakta Entrypoint Script
# Script de inicialização do container Bakta

set -e

echo "========================================"
echo "  PUC Minas - Bakta Container"
echo "========================================"

# Ativar ambiente conda
source /opt/conda/etc/profile.d/conda.sh
conda activate bakta_env

echo ""
echo "🔧 Verificando instalação..."

# Verificar Bakta
if command -v bakta &> /dev/null; then
    BAKTA_VERSION=$(bakta --version 2>&1 | head -1)
    echo "✅ Bakta: $BAKTA_VERSION"
else
    echo "❌ Bakta não encontrado!"
    exit 1
fi

# Verificar/Instalar database
DB_PATH="${BAKTA_DB:-/app/bakta-light}"

echo ""
echo "📦 Verificando database em: $DB_PATH"

if [ ! -d "$DB_PATH" ] || [ -z "$(ls -A $DB_PATH 2>/dev/null)" ]; then
    echo "📥 Database não encontrado. Baixando versão light..."
    echo "   (Isso pode levar alguns minutos na primeira execução)"
    echo ""
    
    mkdir -p "$DB_PATH"
    bakta_db download --type light --output "$DB_PATH"
    
    echo ""
    echo "✅ Database instalado com sucesso!"
else
    echo "✅ Database encontrado"
fi

# Verificar estrutura de diretórios
echo ""
echo "📁 Verificando diretórios..."
mkdir -p /app/data/uploads /app/data/templates /app/resultados
ls -la /app/data /app/resultados

# Verificar Python/Flask
echo ""
echo "🐍 Verificando Python..."
python --version
pip show flask flask-cors | grep -E "^(Name|Version):"

echo ""
echo "========================================"
echo "  Iniciando servidor web..."
echo "========================================"
echo ""
echo "🌐 Acesse: http://localhost:5000"
echo "📊 API: http://localhost:5000/api/status"
echo ""
echo "Pressione Ctrl+C para parar"
echo ""

# Iniciar aplicação Flask
export PYTHONPATH=/app
cd /app/backend
exec python app.py
