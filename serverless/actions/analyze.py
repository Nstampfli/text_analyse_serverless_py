import json
import pandas as pd
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag
from nltk.util import ngrams

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze(params):
    text = params['text']
    sentences = sent_tokenize(text)
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    
    num_sentences = len(sentences)
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    lex_diversity = num_unique_words / num_words
    avg_sentence_length = num_words / num_sentences
    letter_count = Counter(text.lower())
    del letter_count[' ']

    fdist = FreqDist(words)
    word_lengths = [len(word) for word in words]
    length_distribution = FreqDist(word_lengths)
    tags = pos_tag(words)
    pos_counts = FreqDist(tag for (word, tag) in tags)
    bigrams = list(ngrams(words, 2))
    trigrams = list(ngrams(words, 3))
    bigram_freq = FreqDist(bigrams)
    trigram_freq = FreqDist(trigrams)

    results = {
        'letter_count': letter_count,
        'word_frequency': dict(fdist),
        'word_length_distribution': dict(length_distribution),
        'pos_counts': dict(pos_counts),
        'bigram_frequency': dict(bigram_freq),
        'trigram_frequency': dict(trigram_freq),
        'general_statistics': {
            'num_sentences': num_sentences,
            'num_words': num_words,
            'num_unique_words': num_unique_words,
            'lex_diversity': lex_diversity,
            'avg_sentence_length': avg_sentence_length
        }
    }

    return {
        'body': json.dumps(results)
    }
