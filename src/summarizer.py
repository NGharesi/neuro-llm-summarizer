from pydantic import BaseModel, Field

from src.llm_client import LLMClient


class PaperSummary(BaseModel):
    research_question: str = Field(
        description="The main question or hypothesis of the paper."
    )
    methods: str = Field(description="A short description of how the study was run.")
    participants_or_data: str = Field(
        description="Who participated, or what data was analyzed."
    )
    main_findings: str = Field(description="The most important results of the paper.")
    limitations: str = Field(description="Important study limitations.")
    misunderstood_terms: list[str] = Field(
        description="Technical terms a beginner might misunderstand."
    )
    confidence_score: int = Field(
        ge=1,
        le=5,
        description="Confidence score from 1 to 5 based on how clearly the text supports the summary.",
    )


class PaperSummarizer:
    """Coordinates validation and the API call."""

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        self.llm_client = llm_client or LLMClient()
        self.model_name = self.llm_client.model

    def summarize(self, paper_text: str) -> PaperSummary:
        clean_text = paper_text.strip()
        if not clean_text:
            raise ValueError("Paper text cannot be empty.")

        return self.llm_client.get_structured_summary(clean_text, PaperSummary)
