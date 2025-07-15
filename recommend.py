import torch
import pandas as pd
from models.relationship_detector import RelationshipDetector
from models.sentiment_analyzer import SentimentAnalyzer

# Load relationship detector
relationship_model = RelationshipDetector()
relationship_model.model.load_state_dict(torch.load("relationship_model.pth"))
relationship_model.model.eval()

# Load sentiment analyzer
sentiment_model = SentimentAnalyzer()

# Load Spotify data
spotify_df = pd.read_csv("data/spotify-2000.csv")

# Define mapping: relationship → genres
RELATIONSHIP_GENRE_MAP = {
    "romantic-partners": ["pop", "soul", "dance pop"],
    "friends": ["pop", "dance pop", "hip hop"],
    "professional": ["rock", "electronic", "album rock"],
    "siblings": ["pop", "indie pop"],
    "parent-child": ["adult standards", "folk"],
    "myself": ["ambient", "indie pop"]
}

def recommend_song(text):
    # Predict relationship
    relation = relationship_model.predict([text])[0]
    
    # Predict sentiment
    sentiment, confidence = sentiment_model.get_dominant_sentiment(text)
    
    print(f"Detected relationship: {relation}")
    print(f"Detected sentiment: {sentiment} (confidence {confidence:.2f})")
    
    # Get genre preferences for this relationship
    genres = RELATIONSHIP_GENRE_MAP.get(relation, [])
    
    # Filter songs
    filtered_df = spotify_df.copy()
    
    if genres:
        genre_filter = filtered_df["Top Genre"].str.lower().apply(
            lambda g: any(genre in g for genre in genres)
        )
        filtered_df = filtered_df[genre_filter]
    
    # Apply year filtering based on relationship
    if relation in ["siblings", "myself"]:
        # Keep only songs from 2015 onwards
        filtered_df = filtered_df[filtered_df["Year"] >= 2015]
    elif relation == "parent-child":
        # Keep only songs before 2010
        filtered_df = filtered_df[filtered_df["Year"] < 2010]
    # Other relationships → no year filtering
    
    # Filter by sentiment valence
    if sentiment == "positive":
        filtered_df = filtered_df[filtered_df["Valence"] > 50]
    elif sentiment == "negative":
        filtered_df = filtered_df[filtered_df["Valence"] < 50]
    else:
        pass  # neutral → keep all
    
    if filtered_df.empty:
        return "Sorry, no suitable song found."
    
    # Pick a random song
    recommended = filtered_df.sample(1).iloc[0]
    
    title = recommended["Title"]
    artist = recommended["Artist"]
    genre = recommended["Top Genre"]
    
    return f"🎵 Recommended Song: **{title}** by {artist} ({genre})"

# EXAMPLE
if __name__ == "__main__":
    user_input = input("Enter your text: ")
    song = recommend_song(user_input)
    print(song)
