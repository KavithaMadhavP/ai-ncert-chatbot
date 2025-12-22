# AI NCERT Chatbot Tutor

An AI-powered NCERT chatbot tutor built using sentence transformers, semantic search, and confidence-based answer filtering.

---

## 📌 Features
- Answers NCERT Science questions (Classes 6–10)
- Text and voice input support
- Semantic search using embeddings
- Confidence-based answer filtering
- Rejects non-NCERT / out-of-syllabus questions

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- NLP (Semantic Search)
- Speech-to-Text

---

## 📂 Project Structure

ai-ncert-chatbot/
│
├── app.py                     # Main Streamlit application
│
├── utils/
│   └── file_loader.py         # Loads NCERT chapter text files
│
├── nlp/
│   └── answer_engine.py       # Semantic search + confidence scoring
│
├── services/
│   └── speech_service.py      # Converts voice input to text
│
├── data/
│   └── ncert/
│       ├── chapter1.txt
│       ├── chapter2.txt
│       └── ...
│
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── LICENSE

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KavithaMadhavP/ai-ncert-chatbot.git
cd ai-ncert-chatbot

###2️⃣ Create a Virtual Environment
python -m venv venv

###3️⃣ Activate the Virtual Environment

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

###4️⃣ Install Dependencies
pip install -r requirements.txt

###5️⃣ Run the Application
streamlit run app.py

