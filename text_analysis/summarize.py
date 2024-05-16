import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from utils.cleanup import clean_outputs

nltk.download('stopwords')
nltk.download('punkt')

def summarize_text_main(text):
    summary = summarize_text(text)
    save_summary(summary)

def summarize_text(text, min_sentences=2, max_sentences=15):
    sentences = sent_tokenize(text)
    total_sentences = len(sentences)
    num_sentences = max(min_sentences, min(max_sentences, total_sentences // 2))
    
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    freq = FreqDist(words)
    
    ranking = {sentence: sum(freq[word] for word in word_tokenize(sentence)) for sentence in sentences}
    summary_sentences = sorted(ranking, key=ranking.get, reverse=True)[:num_sentences]
    
    summary_sentences = summary_sentences[:max_sentences] if len(summary_sentences) > max_sentences else summary_sentences
    summary_sentences = summary_sentences if len(summary_sentences) >= min_sentences else sentences[:min_sentences]
    
    return ' '.join(summary_sentences)

def save_summary(summary, file_path='outputs/summary.txt'):
    with open(file_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(summary)

if __name__ == '__main__':
    from utils.file_operations import read_text_file
    clean_outputs()
    text = read_text_file('data/source_text.txt')
    summarize_text_main(text)
