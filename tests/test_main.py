import pytest
from src.searcher import extract_articles
from src.summariser import summarise_text


def test_extract_articles_returns_list():
    """Test that extract_articles returns a list."""
    mock_results = {
        "results": [
            {"title": "Test Article", "url": "https://test.com",
             "content": "Test content", "score": 0.9}
        ]
    }
    articles = extract_articles(mock_results)
    assert isinstance(articles, list)
    assert len(articles) == 1


def test_extract_articles_empty_results():
    """Test extract_articles handles empty results."""
    mock_results = {"results": []}
    articles = extract_articles(mock_results)
    assert articles == []


def test_summarise_short_text():
    """Test that short text is returned as is without summarisation."""
    short_text = "Short text."
    result = summarise_text(short_text)
    assert isinstance(result, str)
    assert len(result) > 0
