# AI NCERT Chatbot Tutor

An AI-powered NCERT chatbot tutor that answers Science questions (Classes 6–10) using semantic search and confidence-based answer filtering.


---

## 📌 Features
- Answers NCERT Science questions (Classes 6–10)
- Supports text and voice input
- Semantic search using sentence embeddings
- Confidence-based answer filtering
- Rejects out-of-syllabus / non-NCERT questions

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


## 🚀 Usage
- Ask NCERT Science questions via text or voice
- The chatbot searches NCERT content using semantic similarity
- Answers are displayed only if confidence exceeds a threshold

## 📜 License
This project is licensed under the MIT License.


