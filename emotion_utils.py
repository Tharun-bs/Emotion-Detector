from transformers import pipeline

# Load model only once
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Opposite emotion mapping (you can expand this)
opposite_emotion = {
    "joy": "Try reflecting on calm or peaceful thoughts.",
    "anger": "Try to focus on staying calm and composed.",
    "sadness": "Try doing something that brings you joy.",
    "fear": "Try to feel safe and confident.",
    "surprise": "Try to seek stability and routine.",
    "disgust": "Try focusing on appreciation or gratitude.",
    "neutral": "Try to feel some excitement or joy."
}

def analyze_emotion(text):
    result = classifier(text)[0][0]  # Take the top emotion
    emotion = result['label'].lower()
    suggestion = opposite_emotion.get(emotion, "Stay balanced.")
    return emotion.capitalize(), suggestion
