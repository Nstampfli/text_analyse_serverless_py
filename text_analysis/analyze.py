import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag
from nltk.util import ngrams
import pandas as pd
from collections import Counter
from utils.cleanup import clean_outputs

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_text(text):
    from utils.text_processing import clean_and_tokenize_text
    
    sentences = sent_tokenize(text)
    words = clean_and_tokenize_text(text)
    
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

    with pd.ExcelWriter('outputs/text_analysis.xlsx') as writer:
        pd.DataFrame.from_dict(letter_count, orient='index', columns=['Count']).to_excel(writer, sheet_name='Letter Count')
        pd.DataFrame.from_dict(fdist, orient='index', columns=['Frequency']).sort_values(by='Frequency', ascending=False).to_excel(writer, sheet_name='Word Frequency')
        pd.DataFrame.from_dict(length_distribution, orient='index', columns=['Frequency']).to_excel(writer, sheet_name='Word Length Distribution')
        pd.DataFrame.from_dict(pos_counts, orient='index', columns=['Count']).to_excel(writer, sheet_name='POS Tags')
        pd.DataFrame.from_dict(bigram_freq, orient='index', columns=['Frequency']).to_excel(writer, sheet_name='Bigram Frequency')
        pd.DataFrame.from_dict(trigram_freq, orient='index', columns=['Frequency']).to_excel(writer, sheet_name='Trigram Frequency')

        summary_df = pd.DataFrame({
            'Statistique': ['Nombre de phrases', 'Nombre de mots', 'Nombre de mots uniques', 'Diversité lexicale', 'Longueur moyenne de phrase'],
            'Valeur': [num_sentences, num_words, num_unique_words, lex_diversity, avg_sentence_length]
        })
        summary_df.to_excel(writer, sheet_name='General Statistics', index=False)

if __name__ == '__main__':
    from utils.file_operations import read_text_file
    clean_outputs()
    text = read_text_file('data/source_text.txt')
    analyze_text(text)
