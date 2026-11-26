# Advisor Help Desk Agent

## Project
AI help desk for a fictional financial planning firm (Juniper Ridge Financial),
built in Microsoft Copilot Studio and Power Automate. Staff ask policy questions;
the agent answers from data/policies with citations, drafts client replies that a
manager approves through Power Automate, escalates what it can't answer, and logs
every request to Excel. This repo holds the design docs, synthetic data, test set
and results, exported agent configuration and flows, and documentation.

## My goal
I am learning Copilot Studio and Power Automate hands-on. I build the agent and
flows myself in the Microsoft web tools. Help me prepare documents and data,
check my work, and explain Microsoft concepts in plain language. Check current
Microsoft documentation before answering product questions.

## Rules
- Never run git commit, git push, or rewrite git history. When a change is
  ready, suggest a commit message; I commit myself.
- All commits are under my GitHub identity only. Never add a Claude co-author
  line or any AI attribution to commit messages.
- Zero cost: free tools and free trials only. Flag anything that needs payment.
- Synthetic data only. Never add real names, account numbers or client data.
- Before I commit exported agent or flow files, check them for anything that
  identifies my account or tenant.
- Plain, professional writing. No tutorial or interview-prep notes in files.
- Work one step at a time and stop at each checkpoint for my confirmation.

## Commands
- Generate request history: uv run python scripts/generate_request_history.py

## Current stage
Stage 1, step 1: repo setup