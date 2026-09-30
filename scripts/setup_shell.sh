#!/usr/bin/env bash
# Runs once when the Codespace is created. Makes sure every terminal can see the
# class key, even in the rare case Codespaces has not exported it yet.
marker="# ut-mstc: load class key"
grep -qF "$marker" ~/.bashrc 2>/dev/null && exit 0
cat >> ~/.bashrc <<'EOF'

# ut-mstc: load class key
if [ -z "$ANTHROPIC_API_KEY" ] && [ -f /workspaces/.codespaces/shared/.env ]; then
  _line="$(grep -m1 '^ANTHROPIC_API_KEY=' /workspaces/.codespaces/shared/.env)"
  [ -n "$_line" ] && export "$_line"
  unset _line
fi
EOF
