from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text: str) -> dict:
    """Return sentiment label plus TextBlob polarity and subjectivity."""
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 3)
    subjectivity = round(blob.sentiment.subjectivity, 3)

    if polarity > 0.05:
        label = "Positive"
        emoji = "😊"
    elif polarity < -0.05:
        label = "Negative"
        emoji = "😞"
    else:
        label = "Neutral"
        emoji = "😐"

    return {
        "label": label,
        "emoji": emoji,
        "polarity": polarity,
        "subjectivity": subjectivity,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            result = analyze_sentiment(text)

    return render_template("index.html", result=result, text=text)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
