import streamlit as st
import cv2
import webbrowser
from modules.advanced_emotion import detect_emotion
from modules.recommend import get_recommendation

st.set_page_config(page_title="Emotion AI", layout="centered")

st.title("😊 Emotion AI Assistant")
st.write("Detect your emotion and get smart recommendations")

# Start button
run = st.button("Start Camera")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

emotion_history = []

while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Camera not working")
        break

    try:
        # 🔥 Detect emotion
        emotion, confidence = detect_emotion(frame)

        # 🔥 Filter + store
        if confidence > 0.5:
            emotion_history.append(emotion)
        else:
            emotion_history.append("neutral")

        if len(emotion_history) > 15:
            emotion_history.pop(0)

        # 🔥 Smooth result
        display_emotion = max(set(emotion_history), key=emotion_history.count)

    except:
        display_emotion = "neutral"

    # 🔥 Get recommendation
    recommendation = get_recommendation(display_emotion)

    # Show camera
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

    # Show emotion
    st.subheader(f"Detected Emotion: {display_emotion}")

    # Show content
    st.markdown("### 🎵 Song")
    st.write(recommendation["songs"][0])

    st.markdown("### 🎥 Video")
    st.write(recommendation["videos"][0])

    st.markdown("### 🎧 Podcast")
    st.write(recommendation["podcasts"][0])

    st.markdown("### 📖 Story")
    st.success(recommendation["story"])

    st.markdown("### 💡 Advice")
    st.info(recommendation["advice"])

    # 🔥 Buttons (ONLY here we open links)
    if st.button("🎵 Play Song"):
        webbrowser.open(recommendation["songs"][0])

    if st.button("🎥 Watch Video"):
        webbrowser.open(recommendation["videos"][0])

    if st.button("🎧 Listen Podcast"):
        webbrowser.open(recommendation["podcasts"][0])