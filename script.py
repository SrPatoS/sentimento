import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

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
    sentimento = analisar_sentimento(texto)
    print(f"O sentimento do texto é: {sentimento}")

