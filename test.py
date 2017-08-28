import nltk
from nltk import word_tokenize


def test():

    text = word_tokenize("And now for something completely different")
    print nltk.pos_tag(text)

test()