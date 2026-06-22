import logging
from transformers import pipeline

log = logging.getLogger(__name__)
_summariser = None


def get_summariser():
    """Load summarisation model once and reuse it."""
    global _summariser
    if _summariser is None:
        log.info("Loading summarisation model...")
        _summariser = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            max_length=150,
            min_length=50
        )
    return _summariser


def summarise_text(text: str) -> str:
    """Summarise a given text using BART model."""
    if not text or len(text.strip()) < 100:
        return text
    log.info("Summarising text...")
    try:
        summariser = get_summariser()
        result = summariser(text[:1024], truncation=True)
        return result[0]["summary_text"]
    except Exception as e:
        log.error(f"Summarisation failed: {e}")
        return text[:300] + "..."


def summarise_articles(articles: list) -> list:
    """Summarise all articles from search results."""
    summarised = []
    for article in articles:
        summary = summarise_text(article["content"])
        summarised.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary,
            "score": article["score"]
        })
    return summarised
