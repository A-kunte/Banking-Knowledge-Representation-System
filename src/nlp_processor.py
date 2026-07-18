import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def process_text(text):

    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    print("\nTokens:")
    print(tokens)

    print("\nPOS Tags:")
    print(pos_tags)

    return tokens, pos_tags