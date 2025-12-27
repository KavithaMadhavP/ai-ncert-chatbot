from nlp.embedding_engine import get_best_match
from utils.logger import logger


def find_answer(question, chapters):

    if not chapters:
        return "NCERT data not loaded properly."

    documents = []
    for ch in chapters:
        text = (
            ch.get("chapter_name", "") + " " +
            ch.get("summary", "") + " " +
            " ".join(ch.get("key_points", []))
        )
        documents.append(text)

    if not documents:
        return "No searchable content found."

    index, score = get_best_match(question, documents)

    # 🔐 Confidence threshold
    if score < 0.4:
        return "❌ Sorry, I couldn't find a confident answer in NCERT yet."

    chapter = chapters[index]
    confidence = round(score * 100, 2)

    logger.info(
    f"Question: {question} | "
    f"Chapter: {chapter['chapter_name']} | "
    f"Confidence: {confidence}%"
)


    return (
        f"📘 Chapter: {chapter['chapter_name']}\n"
        f"📊 Confidence: {confidence}%\n\n"
        f"{chapter['summary']}\n\n"
        f"🔑 Key Points:\n- " + "\n- ".join(chapter["key_points"]) +
        f"\n\n🧪 Example:\n{chapter['example']}"
    )
