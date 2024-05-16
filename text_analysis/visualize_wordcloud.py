import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
from utils.cleanup import clean_outputs

nltk.download('punkt')

def generate_wordcloud_main(text):
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    fdist = FreqDist(words)
    generate_wordcloud(fdist)

def generate_wordcloud(frequencies):
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(frequencies)
    wordcloud.to_file('outputs/wordcloud.png')

if __name__ == '__main__':
    from utils.file_operations import read_text_file
    clean_outputs()
    text = read_text_file('data/source_text.txt')
    generate_wordcloud_main(text)
