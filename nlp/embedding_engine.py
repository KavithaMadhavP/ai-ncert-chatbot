from sentence_transformers import SentenceTransformer, util

# Load model once (industry best practice)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_best_match(question, documents):
    """
    Returns index and similarity score of best matching document
    """

    # Convert text to embeddings
    question_embedding = model.encode(question, convert_to_tensor=True)
    doc_embeddings = model.encode(documents, convert_to_tensor=True)

    # Compute cosine similarity
    similarity_scores = util.cos_sim(question_embedding, doc_embeddings)[0]

    best_index = int(similarity_scores.argmax())
    best_score = float(similarity_scores[best_index])

    return best_index, best_score
