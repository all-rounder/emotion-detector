"""Module providing a function printing python version."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emo_detector():
    """Function detect emotion"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        output = "Invalid text! Please try again!"
    else:
    # Return a formatted string
        output = f"""For the given statement, the system response is 'anger': {response['anger']},
        'disgust': {response['disgust']}, 'fear': {response['fear']},
        'joy': {response['joy']} and 'sadness': {response['sadness']}.
        The dominant emotion is joy."""

    return output


@app.route("/")
def render_index_page():
    """Function render index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
