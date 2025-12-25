# AI-Powered NCERT Chatbot Tutor


An industry-ready AI-powered chatbot designed to answer NCERT Science questions 
(Classes 6–10) using semantic search and transformer-based sentence embeddings. 
The system supports both text and voice input and prevents hallucinated responses 
using confidence-based filtering.


---

## ✨ Features
- Answers NCERT Science questions (Classes 6–10)
- Transformer-based semantic search (Sentence Transformers)
- Confidence-based answer filtering to avoid hallucinations
- Text and voice input support
- Domain-restricted responses (NCERT-only)
- Modular and scalable architecture
- Logging for monitoring and debugging

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Sentence Transformers (MiniLM)
- Cosine Similarity
- SpeechRecognition
- NLP (Semantic Search)



---

## 📂 Project Structure

ai-ncert-chatbot/
│
├── app.py                     # Main Streamlit application
│
├── utils/
│   └── file_loader.py         # Loads NCERT chapter data
│
├── nlp/
│   ├── answer_engine.py       # Answer logic + confidence filtering
│   └── embedding_engine.py   # Sentence Transformer embeddings
│
├── services/
│   └── speech_service.py      # Voice-to-text conversion
│
├── data/
│   └── ncert/
│       └── science.json       # NCERT dataset
│
├── logs/
│   └── app.log                # Application logs
│
├── requirements.txt
├── README.md
└── LICENSE


---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KavithaMadhavP/ai-ncert-chatbot.git
cd ai-ncert-chatbot


### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv

Windows
venv\Scripts\activate

Mac / Linux
source venv/bin/activate

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

### 4️⃣ Run the Application
```bash
streamlit run app.py


---

## 🚀 7. Streamlit Cloud Deployment (LIVE)

```md
---

## 🚀 Deployment (Streamlit Cloud)

The AI NCERT Chatbot Tutor is deployed live using **Streamlit Community Cloud**, enabling real-time access through a web browser without local setup.

### Deployment Steps:
1. Push the complete project to GitHub
2. Navigate to https://streamlit.io/cloud
3. Click on **New App**
4. Configure the deployment:
   - Repository: `ai-ncert-chatbot`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **Deploy**

### 🔗 Live Application:
https://ai-ncert-chatbot.streamlit.app

## 🧠 System Architecture

User Input (Text / Voice)
        ↓
Speech-to-Text Service
        ↓
Answer Engine
        ↓
Sentence Transformer Embeddings
        ↓
Cosine Similarity Scoring
        ↓
Confidence Filtering
        ↓
NCERT Answer / Safe Response

## 🎯 Use Cases
- AI tutor for school students
- NCERT exam preparation assistant
- Voice-enabled educational chatbot
- Semantic search over textbook data

## 🔮 Future Enhancements
- FAISS vector database for large-scale data
- Multilingual support
- LLM integration (GPT / Gemini)
- Student performance analytics dashboard
- Teacher/admin interface

git remote add origin https://github.com/KavithaMadhavP/ai-ncert-chatbot.git
git branch -M main
git push -u origin main



## 📜 License
This project is licensed under the MIT License.


