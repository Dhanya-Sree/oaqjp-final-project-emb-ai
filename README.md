# Emotion Detector — Final Project

A Flask web application that uses the Watson NLP **EmotionPredict** service to analyse the emotion in customer feedback text.

---

## Project Structure

```
EmotionDetection/
├── emotion_detection.py   # emotion_detector function
└── __init__.py            # package definition

test_emotion_detection.py  # unit tests
server.py                  # Flask app — route /emotionDetector, port 5000
templates/index.html       # front-end HTML (from starter repo)
static/mywebscript.js      # front-end JavaScript (from starter repo)
```

---

## Setup & Run

**Install dependencies**

```bash
python3 -m pip install requests flask pylint
```

**Run unit tests**

```bash
python3 test_emotion_detection.py
```

**Start the server**

```bash
python3 server.py
```

Then open [http://localhost:5000](http://localhost:5000) in a browser.

> **Note:** Run this inside the Skills Network Theia Lab. The Watson NLP API is only accessible from that environment.

---

## Output

The app returns scores for the following emotions:

- anger
- disgust
- fear
- joy
- sadness

It also reports the **dominant emotion**. If the input text is blank, the response is:

```
Invalid text! Please try again!
```

## Author
Dhanya R