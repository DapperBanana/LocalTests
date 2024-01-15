
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample dataset
dataset = pd.DataFrame({
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Fight Club'],
    'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama'],
    'Director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino', 'David Fincher'],
    'Description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 
                    'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                    'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                    'The lives of two mob hitmen, a boxer, a gangster & his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                    'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.']
})

# Compute the cosine similarity
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(dataset['Genre'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# Function to get recommendations based on similarity scores
def get_recommendations(title, cosine_sim, dataset):
    indices = pd.Series(dataset.index, index=dataset['Title']).drop_duplicates()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return dataset['Title'].iloc[movie_indices]

# Test the recommendation system
title = 'The Shawshank Redemption'
recommendations = get_recommendations(title, cosine_sim, dataset)
print(f"Recommended movies for '{title}':\n{recommendations}")
