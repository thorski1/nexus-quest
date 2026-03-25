#!/usr/bin/env bash
# NEXUS Quest — Installer
# Usage: curl -sSL https://raw.githubusercontent.com/thorski1/nexus-quest/main/install.sh | bash

set -e

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${CYAN} _   _  _______   ___   _ _____  ${NC}"
echo -e "${CYAN}| \\ | ||  ___\\ \\ / / | | /  ___| ${NC}"
echo -e "${CYAN}|  \\| || |__  \\ V /| | | \\ \`--.  ${NC}"
echo -e "${CYAN}| . \` ||  __| /   \\| | | |\`--. \\ ${NC}"
echo -e "${CYAN}| |\\  || |___/ /^\\ \\ |_| /\\__/ / ${NC}"
echo -e "${CYAN}\\_| \\_/\\____/\\/   \\/\\___/\\____/  ${NC}"
echo ""
echo -e "  ${CYAN}NEXUS Quest — Installer${NC}"
echo ""

# ── Detect Python 3.10+ ───────────────────────────────────────────────────────
PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VER=$("$cmd" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "0.0")
        MAJ=$(echo "$VER" | cut -d. -f1)
        MIN=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJ" -gt 3 ] || { [ "$MAJ" -eq 3 ] && [ "$MIN" -ge 10 ]; }; then
            PYTHON="$cmd"
            echo -e "  ${GREEN}OK${NC}  Python $VER"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo -e "  ${RED}ERROR:${NC} Python 3.10+ not found."
    echo "  Download from: https://python.org/downloads"
    exit 1
fi

# ── Install via pipx (preferred) or pip ───────────────────────────────────────
if command -v pipx &>/dev/null; then
    echo "  Installing with pipx..."
    pipx install nexus-quest 2>/dev/null || pipx upgrade nexus-quest
    echo -e "  ${GREEN}OK${NC}  Installed!"
else
    echo "  Installing with pip..."
    "$PYTHON" -m pip install --user --quiet nexus-quest
    echo -e "  ${GREEN}OK${NC}  Installed!"

    # Warn if ~/.local/bin is not in PATH
    LOCAL_BIN="$HOME/.local/bin"
    if [[ ":$PATH:" != *":$LOCAL_BIN:"* ]]; then
        PROFILE="~/.zshrc"
        [[ "$SHELL" == *"bash"* ]] && PROFILE="~/.bash_profile"
        echo ""
        echo -e "  ${YELLOW}NOTE:${NC} Run this to add pip's bin directory to your PATH:"
        echo -e "  ${CYAN}echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> $PROFILE && source $PROFILE${NC}"
    fi
fi

# ── Done ───────────────────────────────────────────────────────────────────────
echo ""
echo -e "  ${GREEN}Installation complete!${NC}"
echo ""
echo -e "  Run the full campaign:  ${CYAN}nexus-quest${NC}"
echo ""
echo "  Standalone packs:"
echo -e "    ${CYAN}terminal-quest${NC}    Bash"
echo -e "    ${CYAN}ssh-quest${NC}         SSH"
echo -e "    ${CYAN}vim-quest${NC}         Vim"
echo -e "    ${CYAN}git-quest${NC}         Git"
echo -e "    ${CYAN}docker-quest${NC}      Docker"
echo -e "    ${CYAN}postgres-quest${NC}    Postgres"
echo -e "    ${CYAN}python-quest${NC}      Python"
echo -e "    ${CYAN}regex-quest${NC}       Regex"
echo -e "    ${CYAN}linux-quest${NC}       Linux"
echo -e "    ${CYAN}kubernetes-quest${NC}  Kubernetes"
echo -e "    ${CYAN}aws-quest${NC}         AWS"
echo ""
echo -e "  Updates install automatically when you run the game."
echo ""
