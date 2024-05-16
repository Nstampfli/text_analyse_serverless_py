import json
from load_text import load_text
from analyze import analyze
from visualize_wordcloud import visualize_wordcloud
from visualize_distributions import visualize_distributions
from summarize import summarize

def main(params):
    load_text_result = load_text({})
    text = load_text_result['text']

    analyze_result = analyze({'text': text})
    analysis = json.loads(analyze_result['body'])

    wordcloud_result = visualize_wordcloud({'text': text})
    wordcloud = json.loads(wordcloud_result['body'])['wordcloud']

    distributions_result = visualize_distributions({'text': text})
    distributions = json.loads(distributions_result['body'])

    summarize_result = summarize({'text': text})
    summary = json.loads(summarize_result['body'])['summary']

    return {
        'body': json.dumps({
            'analysis': analysis,
            'wordcloud': wordcloud,
            'word_length_distribution': distributions['word_length_distribution'],
            'pos_distribution': distributions['pos_distribution'],
            'summary': summary
        })
    }
