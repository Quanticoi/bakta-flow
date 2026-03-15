@echo off
echo ==========================================
echo  PUC Minas - Bakta - GitHub Commit
echo  Desenvolvido por Rui Lima
echo ==========================================
echo.

echo [1/5] Configurando repositorio remoto...
git remote add origin https://github.com/Quanticoi/bakta-local.git 2>nul
git remote set-url origin https://github.com/Quanticoi/bakta-local.git 2>nul
git remote -v
echo.

echo [2/5] Adicionando arquivos ao stage...
git add .
echo Arquivos adicionados!
echo.

echo [3/5] Criando commit...
git commit -m "PUC Minas - Bakta: Plataforma de Anotacao Genomica
echo Desenvolvido por Rui Lima
echo.
echo Inclui:
echo - Backend Flask com API REST
echo - Pipeline Bakta para anotacao genomica
echo - Frontend web com Bootstrap 5
echo - Docker containerization
echo - Documentacao completa
echo - Testes automatizados"
echo.

echo [4/5] Verificando branch...
git branch -M main
echo.

echo [5/5] Fazendo push para GitHub...
echo.
echo ATENCAO: Voce precisara autenticar no GitHub!
echo.
git push -u origin main --force
echo.

echo ==========================================
echo Processo concluido!
echo Repositorio: https://github.com/Quanticoi/bakta-local
echo ==========================================
pause
