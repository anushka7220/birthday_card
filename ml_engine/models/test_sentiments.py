# test_sentiment.py
from sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()

text = "I love this song so much!"
result = analyzer.analyze(text)
print(result)

dominant, confidence = analyzer.get_dominant_sentiment(text)
print(f"Dominant sentiment: {dominant} (confidence {confidence:.4f})")
