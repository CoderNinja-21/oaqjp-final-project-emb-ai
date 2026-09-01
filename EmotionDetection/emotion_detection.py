import json

import requests


def emotion_detector(text_to_analyze):
    """
    Runs emotion detection on the given text using the Watson NLP
    Emotion Predict function.

    Parameters
    ----------
    text_to_analyze : str
        The text to be analysed for emotion.

    Returns
    -------
    dict
        A dictionary containing the scores for anger, disgust, fear,
        joy and sadness, along with the dominant emotion, in the form:
        {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': '<name of the dominant emotion>'
        }
    """

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
        'NlpService/EmotionPredict'
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    # Convert the response text into a dictionary
    response_dict = json.loads(response.text)

    # Extract the emotion scores from the first emotion prediction
    emotions = response_dict['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Determine the dominant emotion (the one with the highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion,
    }