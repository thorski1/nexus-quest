# NEXUS Quest — Windows Installer
# Run from PowerShell with:
#   powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.ps1 | iex"

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  NEXUS Quest — Installer" -ForegroundColor Cyan
Write-Host "  ========================" -ForegroundColor Cyan
Write-Host ""

# ── Find Python 3.10+ ──────────────────────────────────────────────────────────
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

# ── Install via pip ────────────────────────────────────────────────────────────
Write-Host "  Installing nexus-quest..." -ForegroundColor White
& $pythonCmd -m pip install --user --quiet nexus-quest
Write-Host "  OK  Installed!" -ForegroundColor Green

# ── Ensure Scripts directory is in PATH ───────────────────────────────────────
$scriptsDir = & $pythonCmd -c "import sysconfig; print(sysconfig.get_path('scripts'))"
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$scriptsDir*") {
    $newPath = if ($userPath) { "$userPath;$scriptsDir" } else { $scriptsDir }
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "  OK  Added Python Scripts to PATH" -ForegroundColor Green
    Write-Host "  NOTE: Open a new terminal window for PATH to take effect" -ForegroundColor Yellow
} else {
    Write-Host "  OK  Scripts directory already in PATH" -ForegroundColor Green
}

# ── Done ───────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "  Open a NEW terminal window, then run:" -ForegroundColor White
Write-Host "    nexus-quest" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Standalone packs:" -ForegroundColor White
Write-Host "    terminal-quest    Bash" -ForegroundColor DarkCyan
Write-Host "    ssh-quest         SSH" -ForegroundColor DarkCyan
Write-Host "    vim-quest         Vim" -ForegroundColor DarkCyan
Write-Host "    git-quest         Git" -ForegroundColor DarkCyan
Write-Host "    docker-quest      Docker" -ForegroundColor DarkCyan
Write-Host "    postgres-quest    Postgres" -ForegroundColor DarkCyan
Write-Host "    python-quest      Python" -ForegroundColor DarkCyan
Write-Host "    regex-quest       Regex" -ForegroundColor DarkCyan
Write-Host "    linux-quest       Linux" -ForegroundColor DarkCyan
Write-Host "    kubernetes-quest  Kubernetes" -ForegroundColor DarkCyan
Write-Host "    aws-quest         AWS" -ForegroundColor DarkCyan
Write-Host ""
Write-Host "  TIP: Use Windows Terminal for best display." -ForegroundColor Yellow
Write-Host "  Updates install automatically when you run the game." -ForegroundColor Yellow
Write-Host ""
