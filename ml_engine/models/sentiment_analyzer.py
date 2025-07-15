from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Dict, Tuple
import torch

class SentimentAnalyzer:
    def __init__(self):
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        
        self.sentiment_map = {
            0: "negative",
            1: "neutral",
            2: "positive"
        }
    
    def analyze(self, text: str) -> Dict[str, float]:
        """Analyze text sentiment and return scores"""
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        return {
            "negative": probs[0][0].item(),
            "neutral": probs[0][1].item(),
            "positive": probs[0][2].item()
        }
    
    def get_dominant_sentiment(self, text: str) -> Tuple[str, float]:
        """Get the dominant sentiment and its confidence"""
        scores = self.analyze(text)
        dominant = max(scores, key=scores.get)
        return dominant, scores[dominant]