from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models.relationship_detector import RelationshipDetector
from .models.sentiment_analyzer import SentimentAnalyzer
from .recommend import SpotifyRecommender, MemeRecommender

# Initialize models (lazy loading)
relationship_detector = None
sentiment_analyzer = None
spotify_recommender = None
meme_recommender = None

def get_relationship_detector():
    global relationship_detector
    if relationship_detector is None:
        relationship_detector = RelationshipDetector()
    return relationship_detector

def get_sentiment_analyzer():
    global sentiment_analyzer
    if sentiment_analyzer is None:
        sentiment_analyzer = SentimentAnalyzer()
    return sentiment_analyzer

def get_spotify_recommender():
    global spotify_recommender
    if spotify_recommender is None:
        spotify_recommender = SpotifyRecommender('data/spotify_processed.csv')
    return spotify_recommender

def get_meme_recommender():
    global meme_recommender
    if meme_recommender is None:
        meme_recommender = MemeRecommender('data/meme_tags.json')
    return meme_recommender

@csrf_exempt
def analyze_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            # Get relationship
            rel_detector = get_relationship_detector()
            relationship, rel_confidence = rel_detector.predict(message)
            
            # Get sentiment
            sent_analyzer = get_sentiment_analyzer()
            sentiment, sent_confidence = sent_analyzer.get_dominant_sentiment(message)
            
            return JsonResponse({
                'relationship': relationship,
                'relationship_confidence': rel_confidence,
                'sentiment': sentiment,
                'sentiment_confidence': sent_confidence
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_recommendations(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            relationship = data.get('relationship')
            sentiment = data.get('sentiment')
            
            # Get song recommendations
            spotify = get_spotify_recommender()
            songs = spotify.recommend(relationship, sentiment)
            
            # Get meme recommendations
            meme = get_meme_recommender()
            memes = meme.recommend(relationship, sentiment)
            
            return JsonResponse({
                'songs': songs,
                'memes': memes
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)