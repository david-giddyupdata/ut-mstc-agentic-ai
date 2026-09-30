# Agentic AI Workshop: UT MSTC

Your workspace for the workshop. Everything runs in your browser. Nothing to install.

## Start here

1. **Make your own copy.** Click **Use this template > Create a new repository**. Name it `my-agentic-workshop`. The visibility setting starts on **Public**: change it to **Private**. Click **Create repository**.
2. **Add the class key.** Open **github.com > your profile picture > Settings > Codespaces**. In the **Codespace user secrets** section, click **New secret**. Name it `ANTHROPIC_API_KEY` and paste the key from the class email. Under **Repository access**, type `my-agentic` and pick the repository that starts with **your own username** (other people's public repositories can appear in the list too). Click **Add secret**. Do this before step 3.
3. **Launch your workspace.** In your new repository, click **Code > Codespaces > Create codespace on main**. It opens in a new browser tab. The first launch takes about four to five minutes.
4. **Check your setup.** When the editor has finished loading, run this in the terminal at the bottom:

   ```bash
   python scripts/smoke_test.py
   ```

   You should see `SETUP VERIFIED`. If you see `SETUP INCOMPLETE` with several packages `MISSING`, setup is still finishing: wait a minute, open a new terminal with the **+** icon, and run the test again.
5. **Start Claude.** Type `claude` in the terminal and press Enter. (The terminal may suggest typing `copilot`. Ignore that; this workshop uses `claude`.)

When you paste a long prompt into Claude, the first Enter can add a new line instead of sending it. If nothing happens, press Enter again.

## What is in this project

| Path | What it is |
|---|---|
| `data/monthlysummary.csv` | U.S. flight performance by airport and month, 2020 to 2025 (Bureau of Transportation Statistics) |
| `CLAUDE.md` | Standing instructions Claude reads at the start of every session. You fill it in. |
| `.claude/settings.json` | What Claude may do without asking, plus the guardrail hook |
| `.claude/hooks/destructive_guard.py` | The guardrail: Claude must ask before deleting anything |

Never paste the class key into a file in this repository. GitHub scans repositories for keys, and a committed key is disabled within minutes.
