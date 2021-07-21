import spacy

nlp = spacy.load("en_core_web_sm")

def preprocessing(sentence):
    """
    splits sentence into a list of words/tokens.
    a token can be a word, punctuation, or a number.
    """
    doc = nlp(sentence)
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return tokens

tokens = preprocessing("splits sentence into a list of words/tokens.a token can be a word, punctuation, or a number.")
print(tokens)
