import json
from wordcloud import WordCloud
import io
import base64
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

def visualize_wordcloud(params):
    text = params['text']
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    fdist = FreqDist(words)

    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(fdist)
    
    buffer = io.BytesIO()
    wordcloud.to_image().save(buffer, format="PNG")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')

    return {
        'body': json.dumps({
            'wordcloud': img_str
        })
    }
