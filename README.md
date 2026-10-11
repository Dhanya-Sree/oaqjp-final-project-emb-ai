# Emotion Detector — Final Project

A Flask web application that uses the Watson NLP **EmotionPredict** service to analyse the emotion in customer feedback text.

---

## Project Structure

```
oaqjp-final-project-emb-ai/
├── emotion_detection.py      # emotion_detector() — calls Watson NLP API
├── server.py                 # Flask app — route /emotionDetector, port 5001
├── test_emotion_detection.py # unit tests (5 emotion test cases)
├── __init__.py               # package definition
├── templates/
│   └── index.html            # front-end HTML
├── static/
│   └── mywebscript.js        # front-end JavaScript
├── .gitignore
├── LICENSE
└── README.md
```

---

## Required Packages

| Package | Purpose |
|---|---|
| `flask` | Web server and routing |
| `requests` | HTTP calls to the Watson NLP API |
| `pylint` | Code linting (dev) |

**Install all at once:**

```bash
pip3 install flask requests pylint
```

---

## Setup & Run

### 1 — Run unit tests

```bash
python3 -m unittest test_emotion_detection.py
```

Runs 5 test cases covering: `joy`, `anger`, `disgust`, `sadness`, `fear`.

### 2 — Start the Flask server

```bash
python3 server.py
```

Then open [http://localhost:5001](http://localhost:5001) in a browser.

### 3 — Call the API directly

```
GET http://localhost:5001/emotionDetector?textToAnalyze=I+am+so+happy
```

**Sample JSON response:**

```json
{
  "anger": 0.006,
  "disgust": 0.002,
  "fear": 0.009,
  "joy": 0.954,
  "sadness": 0.011,
  "dominant_emotion": "joy"
}
```

If the input text is blank or invalid, the response is:

```
Invalid input!Please try again!.
```

> **Note:** Run this inside the **IBM Skills Network Theia Lab**. The Watson NLP API endpoint is only accessible from that environment.

---

## Author

Dhanya R
