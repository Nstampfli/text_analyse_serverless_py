from nltk.tokenize import word_tokenize

def clean_and_tokenize_text(text):
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    return words
