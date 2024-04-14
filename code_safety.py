
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data
data = {
    'movie_id': [1, 2, 3, 4],
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction'],
    'genre': ['Drama', 'Crime', 'Action', 'Crime']
}

df = pd.DataFrame(data)

# Create tf-idf matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar movies

    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Get recommendations for a given movie
movie_title = 'The Godfather'
recommendations = get_recommendations(movie_title)
print(f"Recommended movies for '{movie_title}':")
print(recommendations)
