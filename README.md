# Neuroscience Paper Summarizer

This project uses an LLM to summarize neuroscience research papers into structured fields.

## Goal

Test how well LLMs summarize neuroscience papers and identify where they may miss technical details.

## Features

- Paste paper text
- Generate structured scientific summary
- Save outputs to CSV
- Prepare results for a mini research paper

## Setup

```bash
git clone YOUR_REPO_LINK
cd neuro-llm-summarizer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
