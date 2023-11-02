import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def NgramsCount(corpus:pd.DataFrame,collum:str="text" ,nintens:int = 1, rank:int=10)-> pd.DataFrame:
    corpus = corpus[collum].apply(str)
    nrange = (nintens,nintens)
    vectorizer = CountVectorizer(ngram_range=nrange).fit(corpus)
    ngrmas_bag = vectorizer.transform(corpus)
    words_freq = [
        (word, ngrmas_bag.sum(axis=0)[0, idx])
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