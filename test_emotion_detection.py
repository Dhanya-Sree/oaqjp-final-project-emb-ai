"""Unit tests for the emotion_detector function."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestDominantEmotions(unittest.TestCase):
    """Tests that emotion_detector returns the correct dominant emotion."""

    def get_emotion(self, text):
        """Helper: return only the dominant emotion for a given text."""
        emotions = emotion_detector(text)
        return emotions.get('dominant_emotion')

    def test_joy(self):
        """Dominant emotion should be joy."""
        dominant_emotion = self.get_emotion('I am glad this happened')
        self.assertEqual(dominant_emotion, 'joy')

    def test_anger(self):
        """Dominant emotion should be anger."""
        dominant_emotion = self.get_emotion('I am really mad about this')
        self.assertEqual(dominant_emotion, 'anger')

    def test_disgust(self):
        """Dominant emotion should be disgust."""
        dominant_emotion = self.get_emotion('I feel disgusted just hearing about this')
        self.assertEqual(dominant_emotion, 'disgust')

    def test_sadness(self):
        """Dominant emotion should be sadness."""
        dominant_emotion = self.get_emotion('I am so sad about this')
        self.assertEqual(dominant_emotion, 'sadness')

    def test_fear(self):
        """Dominant emotion should be fear."""
        dominant_emotion = self.get_emotion('I am really afraid that this will happen')
        self.assertEqual(dominant_emotion, 'fear')


if __name__ == '__main__':
    unittest.main()
