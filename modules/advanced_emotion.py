from deepface import DeepFace
import cv2

def detect_emotion(face):
    try:
        # Convert BGR → RGB
        face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        result = DeepFace.analyze(
                face_rgb,
                actions=['emotion'],
                enforce_detection=False,
                detector_backend='retinaface'   # 🔥 BONUS (better accuracy)
        )

        # Handle result format
        if isinstance(result, list):
            emotions = result[0]['emotion']
        else:
            emotions = result['emotion']

        # Get dominant emotion
        emotion = max(emotions, key=emotions.get)
        confidence = emotions[emotion]

        return emotion, confidence

    except:
        return "neutral", 0