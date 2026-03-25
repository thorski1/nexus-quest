# NEXUS Quest — Windows Installer
# Run from PowerShell with:
#   powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.ps1 | iex"

$ErrorActionPreference = "Stop"
$InstallDir = "$env:LOCALAPPDATA\QuestEngine"

Write-Host ""
Write-Host "  NEXUS Quest Installer" -ForegroundColor Cyan
Write-Host "  =====================" -ForegroundColor Cyan
Write-Host ""

# ── Find Python ────────────────────────────────────────────────────────────────
# Try common Windows Python commands in order of preference
$pythonCmd = $null
foreach ($cmd in @("python", "py", "python3")) {
    try {
        $ver = & $cmd --version 2>&1
        if ($ver -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]
            $minor = [int]$Matches[2]
            if ($major -gt 3 -or ($major -eq 3 -and $minor -ge 10)) {
                $pythonCmd = $cmd
                Write-Host "  OK  Python $major.$minor (via '$cmd')" -ForegroundColor Green
                break
            } else {
                Write-Host "  WARN  Found Python $major.$minor via '$cmd' — need 3.10+" -ForegroundColor Yellow
            }
        }
    } catch { }
}

if (-not $pythonCmd) {
    Write-Host ""
    Write-Host "  ERROR: Python 3.10+ not found." -ForegroundColor Red
    Write-Host "  Download from: https://python.org/downloads" -ForegroundColor Red
    Write-Host "  During install, check 'Add Python to PATH'" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# ── Find git ───────────────────────────────────────────────────────────────────
$gitFound = $false
try {
    $gitVer = git --version 2>&1
    if ($gitVer -match "git version") {
        $gitFound = $true
        Write-Host "  OK  $gitVer" -ForegroundColor Green
    }
} catch { }

if (-not $gitFound) {
    Write-Host ""
    Write-Host "  ERROR: git not found." -ForegroundColor Red
    Write-Host "  Download from: https://git-scm.com/download/win" -ForegroundColor Red
    Write-Host "  During install, choose 'Git from the command line and also from 3rd-party software'" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# ── Create install directory ───────────────────────────────────────────────────
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
Write-Host ""
Write-Host "  Installing to: $InstallDir" -ForegroundColor White
Write-Host ""

# ── Clone or update repos ──────────────────────────────────────────────────────
function Install-Or-Update {
    param ($Name, $Url)
    $dir = Join-Path $InstallDir $Name
    if (Test-Path (Join-Path $dir ".git")) {
        Write-Host "  Updating $Name..." -ForegroundColor White
        git -C $dir pull --quiet 2>&1 | Out-Null
    } else {
        Write-Host "  Cloning $Name..." -ForegroundColor White
        git clone --quiet $Url $dir 2>&1 | Out-Null
    }
    Write-Host "  OK  $Name" -ForegroundColor Green
}

Install-Or-Update "quest-engine" "https://github.com/thorski1/quest-engine.git"
Install-Or-Update "nexus-quest"  "https://github.com/thorski1/nexus-quest.git"

# ── Install Python packages ────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Installing Python packages..." -ForegroundColor White

$engineDir = Join-Path $InstallDir "quest-engine"
$gameDir   = Join-Path $InstallDir "nexus-quest"

& $pythonCmd -m pip install -e $engineDir -q --no-warn-script-location
& $pythonCmd -m pip install -e $gameDir   -q --no-warn-script-location

Write-Host "  OK  packages installed" -ForegroundColor Green

# ── Ensure Scripts directory is in PATH ───────────────────────────────────────
Write-Host ""
Write-Host "  Checking PATH..." -ForegroundColor White

$scriptsDir = & $pythonCmd -c "import sysconfig; print(sysconfig.get_path('scripts'))"

$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$scriptsDir*") {
    $newPath = if ($userPath) { "$userPath;$scriptsDir" } else { $scriptsDir }
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "  OK  Added Python Scripts to PATH: $scriptsDir" -ForegroundColor Green
    Write-Host "  NOTE: Restart this terminal for PATH to take effect" -ForegroundColor Yellow
} else {
    Write-Host "  OK  Scripts directory already in PATH" -ForegroundColor Green
}

# ── Done ───────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "  To play, open a NEW terminal window and run:" -ForegroundColor White
Write-Host "    nexus-quest" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Standalone chapters:" -ForegroundColor White
Write-Host "    terminal-quest   bash" -ForegroundColor DarkCyan
Write-Host "    ssh-quest        SSH" -ForegroundColor DarkCyan
Write-Host "    vim-quest        Vim" -ForegroundColor DarkCyan
Write-Host "    git-quest        Git" -ForegroundColor DarkCyan
Write-Host "    docker-quest     Docker" -ForegroundColor DarkCyan
Write-Host "    postgres-quest   Postgres" -ForegroundColor DarkCyan
Write-Host ""
Write-Host "  TIP: Use Windows Terminal for best display." -ForegroundColor Yellow
Write-Host "  Get it free from the Microsoft Store: search 'Windows Terminal'" -ForegroundColor Yellow
Write-Host ""
