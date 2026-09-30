# Agentic AI Workshop: UT MSTC

Your workspace for the workshop. Everything runs in your browser. Nothing to install.

## Start here

1. **Make your own copy.** Click **Use this template > Create a new repository**. Name it `my-agentic-workshop`, choose **Private**, and click **Create repository**.
2. **Add the class key.** Open **github.com > your profile picture > Settings > Codespaces**. Under **Secrets**, click **New secret**. Name it `ANTHROPIC_API_KEY`, paste the key from the class email, pick `my-agentic-workshop` under **Repository access**, and click **Add secret**.
3. **Launch your workspace.** In your new repository, click **Code > Codespaces > Create codespace on main**. The first launch takes about three minutes.
4. **Check your setup.** When the editor opens, run this in the terminal at the bottom:

   ```bash
   python scripts/smoke_test.py
   ```

   You should see `SETUP VERIFIED`.
5. **Start Claude.** Type `claude` in the terminal and press Enter.

## What is in this project

| Path | What it is |
|---|---|
| `data/monthlysummary.csv` | U.S. flight performance by airport and month, 2020 to 2025 (Bureau of Transportation Statistics) |
| `CLAUDE.md` | Standing instructions Claude reads at the start of every session. You fill it in. |
| `.claude/settings.json` | What Claude may do without asking, plus the guardrail hook |
| `.claude/hooks/destructive_guard.py` | The guardrail: Claude must ask before deleting anything |

Never paste the class key into a file in this repository. GitHub scans repositories for keys, and a committed key is disabled within minutes.
