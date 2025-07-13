from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def is_similar(text1, text2, threshold=0.85):
    vectorizer = TfidfVectorizer().fit([text1, text2])
    vectors = vectorizer.transform([text1, text2])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return score > threshold
