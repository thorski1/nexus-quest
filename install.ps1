# NEXUS Quest Installer for Windows
# Run in PowerShell: irm https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.ps1 | iex

$ErrorActionPreference = "Stop"
$InstallDir = "$env:LOCALAPPDATA\QuestEngine"

Write-Host ""
Write-Host "  NEXUS Quest Installer" -ForegroundColor Cyan
Write-Host "  =====================" -ForegroundColor Cyan
Write-Host ""

# Check Python
try {
    $pyVer = python --version 2>&1
    $match = $pyVer -match "Python (\d+)\.(\d+)"
    if (-not $match) { throw "Python not found" }
    $major = [int]$Matches[1]
    $minor = [int]$Matches[2]
    if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
        Write-Host "  ERROR: Python 3.10+ required (found $pyVer)" -ForegroundColor Red
        Write-Host "  Download from https://python.org/downloads" -ForegroundColor Red
        exit 1
    }
    Write-Host "  OK  Python $major.$minor" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Python not found. Download from https://python.org/downloads" -ForegroundColor Red
    exit 1
}

# Check git
try {
    git --version | Out-Null
    Write-Host "  OK  git found" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: git not found. Download from https://git-scm.com" -ForegroundColor Red
    exit 1
}

# Create install directory
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
Write-Host ""
Write-Host "  Installing to $InstallDir ..." -ForegroundColor White
Write-Host ""

function Install-Or-Update {
    param ($Name, $Url)
    $dir = "$InstallDir\$Name"
    if (Test-Path "$dir\.git") {
        Write-Host "  Updating $Name..."
        git -C $dir pull --quiet
    } else {
        Write-Host "  Cloning $Name..."
        git clone --quiet $Url $dir
    }
}

Install-Or-Update "quest-engine" "https://github.com/thorski1/quest-engine.git"
Install-Or-Update "nexus-quest"  "https://github.com/thorski1/nexus-quest.git"

Write-Host ""
Write-Host "  Installing Python packages..."
pip install -e "$InstallDir\quest-engine" -q
pip install -e "$InstallDir\nexus-quest" -q

Write-Host ""
Write-Host "  Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "  Commands available in your terminal:"
Write-Host "    nexus-quest      - Full 6-chapter campaign"
Write-Host "    terminal-quest   - Bash chapter"
Write-Host "    git-quest        - Git chapter"
Write-Host "    docker-quest     - Docker chapter"
Write-Host "    postgres-quest   - Postgres chapter"
Write-Host "    vim-quest        - Vim chapter"
Write-Host "    ssh-quest        - SSH chapter"
Write-Host ""
Write-Host "  Recommended terminal: Windows Terminal (from Microsoft Store)"
Write-Host ""
