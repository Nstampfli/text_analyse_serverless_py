import json
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('stopwords')
nltk.download('punkt')

def summarize(params):
    text = params['text']
    sentences = sent_tokenize(text)
    total_sentences = len(sentences)
    num_sentences = max(2, min(15, total_sentences // 2))
    
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    freq = FreqDist(words)
    
    ranking = {sentence: sum(freq[word] for word in word_tokenize(sentence)) for sentence in sentences}
    summary_sentences = sorted(ranking, key=ranking.get, reverse=True)[:num_sentences]
    summary_sentences = summary_sentences[:15] if len(summary_sentences) > 15 else summary_sentences
    summary_sentences = summary_sentences if len(summary_sentences) >= 2 else sentences[:2]

    summary = ' '.join(summary_sentences)
    return {
        'body': json.dumps({'summary': summary})
    }
