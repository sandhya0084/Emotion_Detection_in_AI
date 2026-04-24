from fer import FER
import cv2

detector = FER(mtcnn=True)

def detect_emotion(frame):
    try:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = detector.detect_emotions(rgb)

        if result:
            emotions = result[0]["emotions"]
            emotion = max(emotions, key=emotions.get)
            confidence = emotions[emotion]
            return emotion, confidence

        return "neutral", 0

    except:
        return "neutral", 0