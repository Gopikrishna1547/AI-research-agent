import logging
import streamlit as st
from src.searcher import search_web, extract_articles
from src.summariser import summarise_articles
from src.report_generator import generate_report

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("agent.log"), logging.StreamHandler()]
)
log = logging.getLogger(__name__)

st.set_page_config(
    page_title="AI Research Assistant Agent",
    page_icon="AI",
    layout="wide"
)

st.title("AI Research Assistant Agent")
st.markdown("Enter a research topic — the agent will search, summarise, and generate a report.")
st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input(
        "Research topic:",
        placeholder="e.g. Latest developments in RAG systems 2025"
    )
with col2:
    max_results = st.slider("Number of sources", min_value=3, max_value=10, value=5)

if st.button("Run Research Agent", type="primary", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a research topic!")
    else:
        with st.status("Agent is working...", expanded=True) as status:
            st.write("Searching the web...")
            try:
                results = search_web(topic, max_results=max_results)
                articles = extract_articles(results)
                st.write(f"Found {len(articles)} articles.")
            except Exception as e:
                st.error(f"Search failed: {e}")
                st.stop()

            st.write("Summarising articles...")
            try:
                summarised = summarise_articles(articles)
                st.write("Summarisation complete.")
            except Exception as e:
                st.error(f"Summarisation failed: {e}")
                st.stop()

            st.write("Generating PDF report...")
            try:
                report_path = generate_report(topic, summarised)
                st.write("Report saved.")
            except Exception as e:
                st.error(f"Report generation failed: {e}")
                st.stop()

            status.update(label="Research complete!", state="complete")

        st.divider()
        st.subheader("Research Results")
        for i, article in enumerate(summarised, 1):
            with st.expander(f"{i}. {article['title']}", expanded=(i == 1)):
                st.markdown("**Summary:**")
                st.write(article["summary"])
                st.markdown(f"**Source:** [{article['url']}]({article['url']})")

        st.divider()
        st.subheader("Download Report")
        with open(report_path, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name=f"research_report_{topic[:30].replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
else:
    st.info("Enter a topic above and click Run Research Agent to start.")
    st.markdown("### Example topics:")
    st.markdown("""
    - Latest developments in RAG systems 2025
    - Python machine learning frameworks comparison
    - Natural language processing trends 2025
    - LangChain vs LlamaIndex comparison
    - AI agents in production systems
    """)
