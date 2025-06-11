from flask import Flask, render_template, request
from emotion_utils import analyze_emotion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = suggestion = ""
    if request.method == "POST":
        text = request.form["text"]
        if text:
            emotion, suggestion = analyze_emotion(text)
    return render_template("index.html", emotion=emotion, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
