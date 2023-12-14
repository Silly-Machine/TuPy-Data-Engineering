import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def NgramsCount(corpus: pd.DataFrame, column: str = "text", ngrams: int = 1, rank: int = 10) -> pd.DataFrame:
    """
    Count the frequency of n-grams in a text corpus and return the top n-grams.

    Parameters:
    - corpus (pd.DataFrame): The input DataFrame containing the text data.
    - column (str, optional): The column name containing the text data. Default is "text".
    - ngrams (int, optional): The size of n-grams to consider. Default is 1 (unigrams).
    - rank (int, optional): The number of top n-grams to return. Default is 10.

    Returns:
    - pd.DataFrame: A DataFrame with columns "Word"/"Bigram"/"Trigram"/"{ngrams}_gram" and "Frequency".

    Example:
    ```python
    ngrams_df = NgramsCount(my_corpus, column='content', ngrams=2, rank=15)
    print(ngrams_df)
    ```
    """
    corpus = corpus[column].apply(str)
    nrange = (ngrams, ngrams)
    vectorizer = CountVectorizer(ngram_range=nrange).fit(corpus)
    ngrams_bag = vectorizer.transform(corpus)
    words_freq = [
        (word, ngrams_bag.sum(axis=0)[0, idx])
        for word, idx in vectorizer.vocabulary_.items()
    ]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

    if nrange[0] == 1:
        order = "Word"
    elif nrange[0] == 2:
        order = "Bigram"
    elif nrange[0] == 3:
        order = "Trigram"
    else:
        order = f"{str(nrange[0])}_gram"

    return pd.DataFrame(words_freq[:rank], columns=[order, "Frequency"])
