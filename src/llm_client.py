import os

from dotenv import load_dotenv
from openai import OpenAI

from src.prompts import SYSTEM_PROMPT, build_user_prompt


class LLMClient:
    """Small wrapper around the OpenAI client."""

    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        load_dotenv()

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-5.4-nano")

        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY was not found. Create a .env file based on .env.example."
            )

        self.client = OpenAI(api_key=self.api_key)

    def get_structured_summary(self, paper_text: str, response_model):
        """Return a parsed Pydantic object from the Responses API."""

        response = self.client.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_user_prompt(paper_text)},
            ],
            text_format=response_model,
        )

        if response.output_parsed is None:
            raise ValueError("The model did not return a structured summary.")

        return response.output_parsed
