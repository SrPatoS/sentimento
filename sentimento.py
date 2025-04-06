import nltk
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def traduzir_texto(texto, src_lang='pt', dest_lang='en'):
    translator = Translator()
    traducao = translator.translate(texto, src=src_lang, dest=dest_lang)
    return traducao.text

def analisar_sentimento(texto):
    pontuacao = analyzer.polarity_scores(texto)
    if pontuacao['compound'] >= 0.05:
        return 'positivo'
    elif pontuacao['compound'] <= -0.05:
        return 'negativo'
    else:
        return 'neutro'

texto = "I'm irritated"

while True:
    texto = input("Digite algo: ")
    texto = traduzir_texto(texto)
    sentimento = analisar_sentimento(texto)
    print(f"O sentimento do texto é: {sentimento}")

