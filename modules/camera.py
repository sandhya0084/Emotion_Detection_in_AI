import cv2
from modules.advanced_emotion import detect_emotion
from modules.recommend import get_recommendation

def start_camera():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    emotion_history = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        display_emotion = "neutral"

        for (x, y, w, h) in faces:

            # 🔥 Ignore small faces
            if w < 80 or h < 80:
                continue

            face = frame[y:y+h, x:x+w]

            try:
                # 🔥 Run detection every 5 frames (stable)
                if frame_count % 10 == 0:
                    emotion, confidence = detect_emotion(face)
                    print("Emotion:", emotion, "Confidence:", confidence)
                    # 🔥 Confidence filter
                    if confidence > 30:
                        emotion_history.append(emotion)
                    else:
                        emotion_history.append("neutral")

                    # 🔥 Keep last 20 values
                    if len(emotion_history) > 20:
                        emotion_history.pop(0)

                # 🔥 Smooth result
                if emotion_history:
                    display_emotion = max(set(emotion_history), key=emotion_history.count)
                else:
                             display_emotion = "neutral"
                             
                # 🔥 Get recommendation (only display, no auto open)
                recommendation = get_recommendation(display_emotion)

                # 🔥 Draw face box
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # 🔥 Show emotion
                cv2.putText(frame, display_emotion,
                            (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,
                            (0, 255, 0), 2)

                # 🔥 Show short advice
                cv2.putText(frame, recommendation["advice"],
                            (x, y+h+25),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (255, 255, 0), 2)

            except Exception as e:
                print("Error:", e)

        cv2.imshow("Emotion AI Camera", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()