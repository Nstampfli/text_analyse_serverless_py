import json
import matplotlib.pyplot as plt
import io
import base64
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.probability import FreqDist
import pandas as pd

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def visualize_distributions(params):
    text = params['text']
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    word_lengths = [len(word) for word in words]
    tags = pos_tag(words)
    pos_counts = FreqDist(tag for (word, tag) in tags)

    plt.figure(figsize=(10, 6))
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1))
    plt.title('Distribution de la longueur des mots')
    plt.xlabel('Longueur des mots')
    plt.ylabel('Fréquence')
    buffer = io.BytesIO()
    plt.savefig(buffer, format="PNG")
    buffer.seek(0)
    word_length_dist_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    pos_df = pd.DataFrame.from_dict(pos_counts, orient='index', columns=['Count'])
    pos_df.sort_values('Count', ascending=False).plot(kind='bar')
    plt.title('Fréquence des POS Tags')
    plt.ylabel('Fréquence')
    plt.xlabel('POS Tag')
    buffer = io.BytesIO()
    plt.savefig(buffer, format="PNG")
    buffer.seek(0)
    pos_dist_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        'body': json.dumps({
            'word_length_distribution': word_length_dist_str,
            'pos_distribution': pos_dist_str
        })
    }
