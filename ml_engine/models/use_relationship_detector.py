from relationship_detector import RelationshipDetector  # Import your class

# Initialize and load the trained model
detector = RelationshipDetector()
detector.load_model("relationship_model.pth")  # Load your saved weights

# Example prediction
text = "My brother and I went to the movies"
relationship, confidence = detector.predict(text)
print(f"'{text}' => {relationship} (Confidence: {confidence:.2%})")