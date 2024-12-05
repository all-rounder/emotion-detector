import requests
import json


def dominant_emotion(emotion_rating):
    max_emotion = None
    max_value = 0

    for emotion, value in emotion_rating.items():
        if value > max_value:
            max_emotion = emotion
            max_value = value

    return max_emotion


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)

    emotion_rating = formatted_response["emotionPredictions"][0]["emotion"]
    emotion_rating["dominant_emotion"] = dominant_emotion(emotion_rating)
    return emotion_rating


text = "I love this new technology"
emotion_detector(text)
