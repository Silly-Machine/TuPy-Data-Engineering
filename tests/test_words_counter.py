import pandas as pd
import pytest
from src.text.words_counter import NgramsCount

@pytest.fixture
def sample_corpus():
    data = {'text': ["This is a sample text", "Another sample text", "Yet another text"]}
    return pd.DataFrame(data)

def test_default_parameters(sample_corpus):
    result = NgramsCount(sample_corpus)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 6
    assert "Word" in result.columns
    assert "Frequency" in result.columns
