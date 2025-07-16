# 🌊 MarineGuardAI: Marine Species Identifier + Interactive Conservation Simulator

**Built by Samyak More.**

🧠 AI meets environmental awareness in this full-stack project featuring:
- A deep learning-based image classifier for Omani marine life
- A live-deployed Streamlit web app
- An interactive game-style simulator with drag & drop cleanup, quizzes, videos, and a badge system

---

## 🎯 Overview
MarineGuardAI is an educational AI system that identifies **Top 5 common fish species and Top 5 critically endangered marine animal species in Oman** and then guides the user to protect that species through a gamified simulator. This project combines AI, environmental storytelling, and playful interactivity to spread conservation awareness in an engaging way.

---

## 🐠 Features

### ✅ 1. Marine Animal Identifier (Streamlit App)
- Upload an image → AI predicts from 6 species
- Powered by MobileNetV2
- Confidence display + prediction graph
- Supports expansion to 10 species

**Currently trained species:**
- Barracuda
- Mahi Mahi
- Parrotfish
- Sailfish
- Snapper
- Whale Shark (Endangered)

👉 [🔗 Live Streamlit App](https://marineguardai.streamlit.app)

### ✅ 2. Interactive Simulator (Hosted on Netlify)
- Triggered via "Protect This Species" button after AI prediction
- Accepts species as a URL parameter (e.g. `?species=whale_shark`)

👉 [🎮 Try the Simulator](https://frolicking-licorice-54f3a1.netlify.app)

---

## 🎮 Simulator Modules

### 🧼 Level 1: Trash Clean-up Game (Pac-Man style drag)
- User drags trash into bin to clean ocean
- Message appears on success

### 🧠 Level 2: Awareness Quiz
- Species-specific multiple choice question
- Right answer = badge awarded
- Wrong answer = retry or research

### 🎥 Video Section
- Embedded educational YouTube video on marine life or species
- Optional link to WWF or awareness campaigns

### 🏅 Badge System
- After completing quiz, user earns "Marine Guardian Badge"
- Option to expand to multi-species badge collection

---

## 📦 Tech Stack

| Tool/Library         | Purpose                          |
|----------------------|----------------------------------|
| Python               | Core programming                 |
| TensorFlow / Keras   | Deep learning model              |
| Streamlit            | Frontend web app                 |
| HTML/CSS/JS          | Simulator + mini-game frontend   |
| Netlify              | Static site hosting for simulator|
| Git & GitHub         | Version control & collaboration  |

---

## 🚀 Run Locally

```bash
git clone https://github.com/samyiak/MarineGuardAI.git
cd MarineGuardAI
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```
## 🌱 Future Plans
Add 4 more species to classifier (total: 10)

Unlock badge gallery based on saved progress

Expand game with reef maze, net rescue and cleanup levels

Add local language support (Arabic / Hindi)

📬 Contact
Samyak More
📧 samyak.psmore@gmail.com

And Lastly, 
“You don't need to be a marine biologist to protect the ocean. You just need curiosity, code, and compassion.” 
