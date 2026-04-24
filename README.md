# 🎭 Emotion Detection AI with Smart Recommendations

## 📌 Project Overview

This project is an AI-based system that detects human emotions using a webcam and provides personalized recommendations such as:

* 🎵 Songs
* 🎬 Videos
* 🎧 Podcasts
* 💡 Motivational Advice

The system uses deep learning models to analyze facial expressions and enhance user mood through intelligent suggestions.

---

## 🚀 Features

* 😊 Real-time face & emotion detection
* 🎯 Accurate emotion classification (Happy, Sad, Angry, Neutral, etc.)
* 🎵 Mood-based song recommendations
* 🎬 Automatic YouTube video suggestions
* 🎧 Podcast & storytelling suggestions
* 🔊 Voice-based motivational advice
* 🌐 Web interface using Streamlit

---

## 🧠 Technologies Used

* Python
* OpenCV
* DeepFace / FER (Pretrained Models)
* Streamlit (Web App UI)
* pyttsx3 (Text-to-Speech)
* Webbrowser API

---

## 📂 Project Structure

```
Emotion-AI-Project/
│
├── app.py                 # Main Streamlit app
├── modules/
│   ├── camera.py         # Camera & emotion detection
│   ├── advanced_emotion.py
│   ├── recommend.py      # Recommendation system
│   ├── voice.py          # Voice assistant
│
├── assets/               # Images / UI assets
├── requirements.txt      # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/Emotion_Detection_in_AI.git
cd Emotion_Detection_in_AI
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🔹 Run Camera Version

```
python -m modules.camera
```

### 🔹 Run Web App (Streamlit)

```
streamlit run app.py
```

---

## 🎯 How It Works

1. Captures face using webcam
2. Detects emotion using pretrained model
3. Applies smoothing for stable results
4. Maps emotion → recommendations
5. Displays suggestions + voice output

---

## 📊 Future Improvements

* 🔥 Use AffectNet dataset for better accuracy
* 🤖 Add ChatGPT-based conversational assistant
* 📱 Mobile app version
* ☁️ Deploy on cloud (Streamlit / AWS)
* 🎼 Spotify API integration

---

## 👨‍💻 Author

**Gomathi P**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 💡 Share your ideas

---

## 📜 License

This project is for educational purposes.
