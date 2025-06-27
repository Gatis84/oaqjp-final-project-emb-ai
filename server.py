from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze');

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotion_items = [(k, v) for k, v in response.items() if k != 'dominant_emotion']

    emotion_str_parts = [f"'{k}': {v}" for k, v in emotion_items]
    if len(emotion_str_parts) > 1:
        emotion_str = ", ".join(emotion_str_parts[:-1]) + " and " + emotion_str_parts[-1]
    else:
        emotion_str = emotion_str_parts[0]

    return (
        "For the given statement, the system response is {}. "
        "The dominant emotion is {}."
        .format(emotion_str, response['dominant_emotion'])
    )


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)