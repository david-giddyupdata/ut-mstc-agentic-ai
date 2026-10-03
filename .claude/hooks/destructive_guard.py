#!/usr/bin/env python3
"""Guardrail hook: ask before any shell command that deletes, drops, or changes system settings.

Claude Code runs this before every Bash command (see .claude/settings.json, PreToolUse).
It reads the proposed command as JSON on stdin. If the command looks destructive, it
answers "ask", which makes Claude Code pause and ask you to confirm. Otherwise it stays
silent and the command runs.
"""
import json
import re
import sys

RULES = [
    (r"\brm\b", "deletes files"),
    (r"\brmdir\b|\bunlink\b|\bshred\b", "deletes files or folders"),
    (r"os\.remove|os\.rmdir|shutil\.rmtree|\.unlink\(|\.rmdir\(", "deletes files from inside a script"),
    (r"\bdrop\s+(table|database|schema|view)\b", "drops a database object"),
    (r"\btruncate\s+table\b|\bdelete\s+from\b", "deletes rows from a table"),
    (r"\baws\s+s3\s+(rm|rb)\b|\s--delete\b", "deletes cloud data"),
    (r"\bgit\s+(reset\s+--hard|clean\b|push\b.*--force)", "throws away work in git"),
    (r"\bsudo\b|\bchmod\s+-R\b|\bchown\s+-R\b", "changes system settings"),
    (r"\b(kill|pkill|killall)\b", "stops running programs, which can close parts of VS Code"),
]

try:
    event = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)

command = (event.get("tool_input") or {}).get("command", "")
for pattern, effect in RULES:
    if re.search(pattern, command, re.IGNORECASE):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"Guardrail: this command {effect}. Confirm before it runs.",
            }
        }))
        break
sys.exit(0)
