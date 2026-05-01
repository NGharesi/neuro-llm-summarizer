SYSTEM_PROMPT = """
You are a careful neuroscience research assistant.
Read the paper text and produce a concise structured summary.
Only use information found in the text.
If a field is unclear, say "Not clearly stated in the text."
For misunderstood_terms, list technical terms that a beginner might misunderstand.
If there are no such terms, return an empty list.
Keep the writing clear and beginner-friendly.
""".strip()


def build_user_prompt(paper_text: str) -> str:
    return f"""
Summarize the neuroscience paper text below.

Paper text:
{paper_text}
""".strip()
