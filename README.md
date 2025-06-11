# Emotion-Detector
Emotion Interpreter is a web application that detects the dominant emotion expressed in a given sentence and provides a suggestion based on the opposite or balancing emotion.

# 🎭 Emotion Interpreter

A Flask web application that interprets emotions from text using a transformer-based model and suggests a contrasting or balancing emotion as feedback.

---

## 🔍 Features

- Detects emotions from input text (e.g., Joy, Anger, Sadness)
- Provides suggestions based on opposite emotions
- Uses the `j-hartmann/emotion-english-distilroberta-base` model
- Animated, responsive UI with Dark Mode toggle
- Lightweight and easy to run locally

---

## 📦 Requirements

- Python 3.7+
- Flask
- Transformers (Hugging Face)
- Torch (if not auto-installed with Transformers)

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/emotion-interpreter.git
cd emotion-interpreter
