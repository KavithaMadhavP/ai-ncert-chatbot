import streamlit as st

from utils.file_loader import load_ncert_data
from nlp.answer_engine import find_answer
from services.speech_service import audio_to_text


# ---------- UI ----------
st.title("🤖 AI-Powered NCERT Chatbot Tutor")
st.write("Ask NCERT Science questions (Classes 6–10)")


# ---------- Input ----------
query = st.text_input("✍️ Type your question")

st.write("OR")

audio = st.audio_input("🎤 Speak your question")

if audio:
    st.info("Listening...")
    text = audio_to_text(audio.getvalue())

    if text:
        st.success(f"You said: {text}")
        query = text
    else:
        st.error("Could not understand audio")


# ---------- Processing ----------
if query:
    chapters = load_ncert_data()

    if not chapters:
        st.error("❌ NCERT data not loaded. Please check data files.")
    else:
        answer = find_answer(query, chapters)
        st.write("🧠 AI Answer:")
        st.success(answer)
