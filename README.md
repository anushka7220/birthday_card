<img width="1434" height="713" alt="Screenshot 2025-07-12 at 3 44 59 AM" src="https://github.com/user-attachments/assets/8e9b94fe-a1cc-41a2-8d0e-0e953b15b150" />

# 🎉 Birdy - The Birthday Card Creator 🐦

**Birdy** is an interactive and intelligent birthday card creator where a charming bird character helps users create beautiful and personalized digital cards. The application allows users to choose card styles, colors, and borders, write custom birthday messages, and even embed AI-generated **music and memes**. 🐣✨

---

## 🐤 Concept & Storyline

Birdy is a creative little bird who lives in her nest with her eggs. She has a magical job — **creating birthday cards** for people around the world! With her special skills and your creativity, each card becomes a heartwarming and fun-filled memory.

---

## 🧠 Powered by Machine Learning

Our ML models generate:

- 🎵 **Music Recommendations** based on birthday messages
- 😂 **Memes/GIFs** matching the tone or emotion of the message

These personalized additions bring a new level of delight and uniqueness to each birthday card!

---

## 🚀 Features

- 🖌️ **Choose Card Color and Border Styles**
- 📅 **Input Date of Birth**
- ✍️ **Write a Custom Birthday Message**
- 🤖 **AI-generated Music Suggestions**
- 🖼️ **Memes/GIFs from ML model**
- 💾 **Save or Share the Final Card**

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **ML Engine**: Python, Hugging Face Transformers, Pandas, TensorFlow (optional)
- **Deployment**: Coming soon...

---

## 📁 Project Structure
├── birthday_card/ # Django App
├── ml_engine/ # ML logic: music & meme generation
├── manage.py
├── card
├── templates/ # HTML Templates
│ ├── static/ # CSS, JS, Images
├── users



---

## 🧠 ML Highlights

> All ML models are integrated via Hugging Face and local inference.

- **Sentiment & Context Analysis** for generating memes (`cardiffnlp/twitter-roberta-base-sentiment`)
- **Song Matching** model to suggest tunes based on input text/emotion
- Upcoming: 🎤 Text-to-Speech and 🎥 Meme GIF generation

---

## 🖼️ Sneak Peek

![Card Preview](static/card/images/sample_card.png)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/anushka7220/birthday_card.git
cd birthday_card

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the server
python manage.py runserver
```
---

## 🌐 Usage
Visit http://127.0.0.1:8000

Choose your favorite color and card border

Add a message and DOB

Click "Generate" to receive a card with music & memes

Save or share the card!

🧪 Future Enhancements
Drag & drop meme/music positioning

Text-to-Speech birthday wishes

Mobile responsive design

Export to PDF

Login and save card history

## 💖 Creator
Anushka Sharma
🎓 B.Tech, Electrical Engineering | YMCA University
💼 Frontend + ML Enthusiast | Open Source Contributor
🔗 LinkedIn | GitHub | ✉️ anushka7220@gmail.com
