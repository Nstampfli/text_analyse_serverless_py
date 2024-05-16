import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import pandas as pd
from utils.cleanup import clean_outputs

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def generate_distributions(text):
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    word_lengths = [len(word) for word in words]
    tags = pos_tag(words)
    pos_counts = FreqDist(tag for (word, tag) in tags)
    
    plot_word_length_distribution(word_lengths)
    plot_pos_distribution(pos_counts)

def plot_word_length_distribution(word_lengths):
    plt.figure(figsize=(10, 6))
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1))
    plt.title('Distribution de la longueur des mots')
    plt.xlabel('Longueur des mots')
    plt.ylabel('Fréquence')
    plt.savefig('outputs/word_length_distribution.png')
    plt.close()

def plot_pos_distribution(pos_counts):
    pos_df = pd.DataFrame.from_dict(pos_counts, orient='index', columns=['Count'])
    pos_df.sort_values('Count', ascending=False).plot(kind='bar')
    plt.title('Fréquence des POS Tags')
    plt.ylabel('Fréquence')
    plt.xlabel('POS Tag')
    plt.savefig('outputs/pos_distribution.png')
    plt.close()

if __name__ == '__main__':
    from utils.file_operations import read_text_file
    clean_outputs()
    text = read_text_file('data/source_text.txt')
    generate_distributions(text)
