# PUC Minas - Bakta - Push para GitHub
# Desenvolvido por Rui Lima

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  PUC Minas - Bakta - Push para GitHub" -ForegroundColor Cyan
Write-Host "  Desenvolvido por Rui Lima" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$repoUrl = "https://github.com/Quanticoi/bakta-local.git"

# Verificar se o usuário quer usar token
Write-Host "Para fazer push no GitHub, voce precisa se autenticar." -ForegroundColor Yellow
Write-Host ""
Write-Host "Opcoes:" -ForegroundColor White
Write-Host "1. Usar Token de Acesso Pessoal (Personal Access Token)"
Write-Host "2. Usar GitHub CLI (gh)"
Write-Host "3. Ver instrucoes manuais"
Write-Host ""

$option = Read-Host "Escolha uma opcao (1-3)"

switch ($option) {
    "1" {
        $token = Read-Host "Digite seu GitHub Personal Access Token" -AsSecureString
        $tokenPlain = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($token))
        $remoteUrl = "https://$tokenPlain@github.com/Quanticoi/bakta-local.git"
        
        git remote set-url origin $remoteUrl
        git push -u origin main --force
        
        # Reset para URL sem token
        git remote set-url origin $repoUrl
    }
    "2" {
        gh auth login
        git push -u origin main --force
    }
    "3" {
        Write-Host ""
        Write-Host "=== INSTRUCOES MANUAIS ===" -ForegroundColor Green
        Write-Host ""
        Write-Host "1. Gere um token em: https://github.com/settings/tokens"
        Write-Host "2. Execute o comando:"
        Write-Host "   git push https://SEU_TOKEN@github.com/Quanticoi/bakta-local.git main --force" -ForegroundColor White
        Write-Host ""
        Write-Host "Ou configure o GitHub CLI:"
        Write-Host "   gh auth login"
        Write-Host "   git push -u origin main --force"
    }
    default {
        Write-Host "Opcao invalida" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Repositorio: $repoUrl" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
