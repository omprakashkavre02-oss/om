# SentimentScope — Flask Sentiment Analysis

A clean, beginner-friendly NLP web application that analyzes user-entered text with **TextBlob** and classifies it as **Positive, Negative, or Neutral**.

## ✨ Features

- Sentiment classification: Positive / Negative / Neutral
- TextBlob polarity score from **-1 to +1**
- TextBlob subjectivity score from **0 to 1**
- Responsive modern UI
- Character counter and clear button
- Input validation and a lightweight `/health` endpoint
- No database or API key required
- Easy to run locally and deploy

## 🧠 How it works

1. User enters text in the web interface.
2. Flask receives the text through a POST request.
3. TextBlob calculates polarity and subjectivity.
4. A small threshold-based rule maps polarity to a sentiment label:
   - `polarity > 0.05` → Positive
   - `polarity < -0.05` → Negative
   - otherwise → Neutral
5. The result and scores are displayed on the page.

## 🛠️ Tech Stack

- **Python 3.10+**
- **Flask** — web framework
- **TextBlob** — sentiment analysis
- **HTML5 / CSS3 / JavaScript** — frontend

## 📁 Project Structure

```text
sentiment-analysis-flask/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/omprakashkavre02-oss/om.git
cd om/sentiment-analysis-flask
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download TextBlob's required NLTK corpora

```bash
python -m textblob.download_corpora
```

### 5. Start the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## 🧪 Example Inputs

| Input | Expected result |
|---|---|
| `I absolutely love this application!` | Positive |
| `This is the worst experience ever.` | Negative |
| `The meeting starts at 10 AM.` | Neutral |

## 📊 Understanding the Scores

**Polarity** describes the emotional direction of the text. Values closer to `+1` are more positive, while values closer to `-1` are more negative.

**Subjectivity** estimates whether the text is opinion-based. Values near `0` are more objective and values near `1` are more subjective.

> Note: TextBlob is a lightweight rule/lexicon-based approach. It is useful for learning and simple applications, but it should not be treated as a highly accurate production-grade sentiment model for every domain or language.

## 🎓 Academic Use

This project demonstrates:

- Natural Language Processing (NLP)
- Sentiment analysis
- Polarity and subjectivity
- Flask web development
- Basic frontend-backend integration

## 🔮 Future Enhancements

- Sentiment history and charts
- Batch CSV sentiment analysis
- Multilingual sentiment support
- REST API endpoint
- User authentication
- Transformer-based sentiment models for improved accuracy

## 📄 License

This project is available for educational and academic use.
