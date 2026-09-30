#!/usr/bin/env bash
# Runs once when the Codespace is created (postCreateCommand), from the repo root.
# 1. Makes every terminal see the class key, even if Codespaces has not exported it.
# 2. Pre-answers Claude Code's first-run questions (theme, "use this API key?",
#    "trust this folder?") so students land straight at the prompt.
marker="# ut-mstc: load class key"
if ! grep -qF "$marker" ~/.bashrc 2>/dev/null; then
  cat >> ~/.bashrc <<'EOF'

# ut-mstc: load class key
if [ -z "$ANTHROPIC_API_KEY" ] && [ -f /workspaces/.codespaces/shared/.env ]; then
  _line="$(grep -m1 '^ANTHROPIC_API_KEY=' /workspaces/.codespaces/shared/.env)"
  [ -n "$_line" ] && export "$_line"
  unset _line
fi
EOF
fi

WORKSPACE_DIR="$(pwd)" python3 - <<'PY'
import json, os, pathlib
key = os.environ.get("ANTHROPIC_API_KEY", "")
env_file = pathlib.Path("/workspaces/.codespaces/shared/.env")
if not key and env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.startswith("ANTHROPIC_API_KEY="):
            key = line.split("=", 1)[1]
cfg_path = pathlib.Path.home() / ".claude.json"
cfg = json.loads(cfg_path.read_text()) if cfg_path.exists() else {}
cfg["hasCompletedOnboarding"] = True
cfg.setdefault("theme", "dark")
if key.strip():
    responses = cfg.setdefault("customApiKeyResponses", {"approved": [], "rejected": []})
    suffix = key.strip()[-20:]          # Claude Code matches keys by their last 20 characters
    if suffix not in responses.setdefault("approved", []):
        responses["approved"].append(suffix)
    responses["rejected"] = [r for r in responses.get("rejected", []) if r != suffix]
project = cfg.setdefault("projects", {}).setdefault(os.environ["WORKSPACE_DIR"], {})
project["hasTrustDialogAccepted"] = True
cfg_path.write_text(json.dumps(cfg, indent=2))
print("claude first-run answers set;", "key approved" if key.strip() else "NO KEY FOUND", "| trusted:", os.environ["WORKSPACE_DIR"])
PY
