import spacy
import re
from rapidfuzz import fuzz, utils

nlp = spacy.load('es_core_news_sm')

def processing(text: str):
    text = text.replace('_',' ')
    text = remove_puntuaction(text)
    doc = nlp(str(text))
    
    processed_words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    return processed_words


def remove_puntuaction(texto: str):
    return re.sub(r'[^\w\s]', '', texto)

def match(text1: str, text2: str):
    
    from rapidfuzz import fuzz, utils

def fuzzymatch(text1, text2):
    #print(f'texto1: {text1}, texto2: {text2}') 
    return fuzz.partial_ratio(text1, text2, processor=utils.default_process)

