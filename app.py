from pathlib import Path

import streamlit as st

from src.summarizer import PaperSummarizer
from src.utils import load_sample_text, read_saved_summaries, save_summary_to_csv


PROJECT_ROOT = Path(__file__).resolve().parent
SAMPLE_PATH = PROJECT_ROOT / "data" / "input" / "sample_paper.txt"
OUTPUT_PATH = PROJECT_ROOT / "data" / "output" / "summaries.csv"


st.set_page_config(page_title="Neuro LLM Summarizer", layout="wide")

st.title("Neuro LLM Summarizer")
st.write(
    "Paste neuroscience paper text, generate a structured summary with the OpenAI API, "
    "and save the result to CSV."
)

if "paper_text" not in st.session_state:
    st.session_state.paper_text = load_sample_text(SAMPLE_PATH)

left_col, right_col = st.columns(2)

with left_col:
    if st.button("Load sample paper"):
        st.session_state.paper_text = load_sample_text(SAMPLE_PATH)

with right_col:
    if st.button("Clear text"):
        st.session_state.paper_text = ""

paper_text = st.text_area(
    "Neuroscience paper text",
    value=st.session_state.paper_text,
    height=320,
    placeholder="Paste an abstract, introduction, or full paper text here...",
)
st.session_state.paper_text = paper_text

if st.button("Summarize paper", type="primary"):
    if not paper_text.strip():
        st.warning("Please paste some paper text before running the summary.")
    else:
        try:
            summarizer = PaperSummarizer()
            with st.spinner("Summarizing paper text..."):
                summary = summarizer.summarize(paper_text)
                csv_path = save_summary_to_csv(
                    summary=summary,
                    paper_text=paper_text,
                    model_name=summarizer.model_name,
                    output_path=OUTPUT_PATH,
                )

            st.success("Summary created and saved successfully.")

            st.subheader("Structured Summary")
            st.markdown(f"**Research Question**\n\n{summary.research_question}")
            st.markdown(f"**Methods**\n\n{summary.methods}")
            st.markdown(f"**Participants or Data**\n\n{summary.participants_or_data}")
            st.markdown(f"**Main Findings**\n\n{summary.main_findings}")
            st.markdown(f"**Limitations**\n\n{summary.limitations}")

            misunderstood_terms = ", ".join(summary.misunderstood_terms)
            if not misunderstood_terms:
                misunderstood_terms = "None listed."
            st.markdown(f"**Misunderstood Terms**\n\n{misunderstood_terms}")
            st.markdown(f"**Confidence Score**\n\n{summary.confidence_score} / 5")
            st.caption(f"Saved to: {csv_path}")
        except Exception as exc:
            st.error(f"Something went wrong: {exc}")

saved_summaries = read_saved_summaries(OUTPUT_PATH)
if not saved_summaries.empty:
    st.subheader("Saved Summaries")
    st.dataframe(saved_summaries, use_container_width=True)
