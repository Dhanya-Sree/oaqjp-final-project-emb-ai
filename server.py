"""Flask server to detect emotions using Watson NLP."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def root():
    """Render the main application page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Detect emotions from query text and return scores with dominant emotion."""
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
