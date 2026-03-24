#!/usr/bin/env bash
set -e

INSTALL_DIR="$HOME/.local/share/quest-engine-suite"
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}"
echo " ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗"
echo " ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗"
echo " ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║"
echo " ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
echo -e "${NC}"
echo "NEXUS Quest Installer"
echo "====================="
echo ""

# Check Python 3.10+
if ! command -v python3 &>/dev/null; then
    echo -e "${RED}Error: Python 3 not found. Install from https://python.org${NC}"
    exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(echo $PY_VER | cut -d. -f1)
PY_MINOR=$(echo $PY_VER | cut -d. -f2)
if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
    echo -e "${RED}Error: Python 3.10+ required (found $PY_VER). Download from https://python.org${NC}"
    exit 1
fi
echo -e "  ${GREEN}✓${NC} Python $PY_VER"

# Check git
if ! command -v git &>/dev/null; then
    echo -e "${RED}Error: git not found. Install from https://git-scm.com${NC}"
    exit 1
fi
echo -e "  ${GREEN}✓${NC} git found"

# Install / update
mkdir -p "$INSTALL_DIR"

echo ""
echo "Installing to $INSTALL_DIR ..."
echo ""

install_or_update() {
    local name="$1"
    local url="$2"
    local dir="$INSTALL_DIR/$name"
    if [ -d "$dir/.git" ]; then
        echo "  Updating $name..."
        git -C "$dir" pull --quiet
    else
        echo "  Cloning $name..."
        git clone --quiet "$url" "$dir"
    fi
}

install_or_update "quest-engine" "https://github.com/thorski1/quest-engine.git"
install_or_update "nexus-quest"  "https://github.com/thorski1/nexus-quest.git"

echo ""
echo "  Installing Python packages..."
pip3 install -e "$INSTALL_DIR/quest-engine" --break-system-packages -q 2>/dev/null \
    || pip3 install -e "$INSTALL_DIR/quest-engine" -q
pip3 install -e "$INSTALL_DIR/nexus-quest" --break-system-packages -q 2>/dev/null \
    || pip3 install -e "$INSTALL_DIR/nexus-quest" -q

echo ""
echo -e "${GREEN}Installation complete!${NC}"
echo ""
echo "Commands available:"
echo "  nexus-quest      — Full 6-chapter campaign"
echo "  terminal-quest   — Bash chapter"
echo "  git-quest        — Git chapter"
echo "  docker-quest     — Docker chapter"
echo "  postgres-quest   — Postgres chapter"
echo "  vim-quest        — Vim chapter"
echo "  ssh-quest        — SSH chapter"
echo ""
echo "If commands are not found, add Python's bin to your PATH:"
echo '  export PATH="$HOME/.local/bin:$PATH"'
echo ""
