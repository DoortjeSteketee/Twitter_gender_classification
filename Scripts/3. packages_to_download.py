## Packages that need to be downloaded

import spacy
nlp = spacy.load('en')

import nltk
nltk.downloader.download('vader_lexicon')
from spacy.tokens import Doc
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()
