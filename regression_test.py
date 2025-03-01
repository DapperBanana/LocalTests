
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
documents = [
    "This is a sample document about machine learning",
    "Machine learning is a subfield of artificial intelligence",
    "Python is a popular programming language for machine learning",
    "Deep learning is a type of machine learning algorithm"
]

# Create a CountVectorizer object
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(X, X)

# Function to recommend documents based on input query
def recommend(query, n=1):
    query_vec = vectorizer.transform([query])
    sim_scores = cosine_similarity(query_vec, X).flatten()
    best_indices = sim_scores.argsort()[-n-1:-1][::-1]
    for i in best_indices:
        print(f"Recommendation {n-i}: {documents[i]}")

# Main program
query = "Python programming for machine learning"
recommend(query, n=2)
