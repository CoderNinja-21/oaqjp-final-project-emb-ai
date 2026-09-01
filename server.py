"""
server.py

A Flask web application that exposes an /emotionDetector endpoint.
Given a piece of text, it runs emotion detection using the
EmotionDetection package and returns a formatted description of the
detected emotion scores and the dominant emotion.
"""

from flask import Flask, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Reads the 'textToAnalyze' query parameter, runs emotion detection
    on it, and returns a formatted string describing the emotion
    scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    dominant_emotion = result['dominant_emotion']

    # If the dominant emotion is None, the input text was invalid
    # (e.g. blank), so return an error message with a 400 status code.
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']

    response_text = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    