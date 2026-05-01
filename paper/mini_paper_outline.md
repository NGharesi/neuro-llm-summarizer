# Mini Paper Outline

## Working Title

Using Large Language Models to Produce Structured Summaries of Neuroscience Papers

## 1. Introduction

- Why neuroscience papers can be difficult for beginners to read
- Why structured summaries are useful for learning and review
- Why an LLM-based workflow can help

## 2. Project Goal

- Build a simple app that accepts neuroscience paper text
- Generate a structured summary with fixed fields
- Save outputs for later review in CSV format

## 3. Methods

- Streamlit for the user interface
- OpenAI API for summary generation
- Pydantic for the structured schema
- pandas for CSV storage
- python-dotenv for local environment variables

## 4. Expected Output

- Research question
- Methods
- Participants or data
- Main findings
- Limitations
- Misunderstood terms
- Confidence score

## 5. Limitations

- Output quality depends on the pasted source text
- The model may miss context if the paper text is incomplete
- Confidence scores are estimates, not ground truth

## 6. Future Improvements

- Upload PDF support
- Export to JSON
- Add citation extraction
- Compare multiple papers side by side
