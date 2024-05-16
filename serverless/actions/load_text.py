import json

def load_text(params):
    with open('data/source_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    return {
        'text': text
    }
