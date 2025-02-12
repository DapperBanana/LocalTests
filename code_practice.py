
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
items = {
    'item1': [1, 0, 1, 0, 1],
    'item2': [0, 1, 0, 1, 0],
    'item3': [1, 1, 0, 1, 0],
    'item4': [0, 1, 1, 0, 1],
}

# Function to calculate similarity between items
def calculate_similarity(item1, item2):
    return cosine_similarity([item1], [item2])[0][0]

# Function to recommend items based on user preferences
def content_based_recommendation(user_preferences, items):
    recommendations = {}
    for item_name, item_vector in items.items():
        similarity = calculate_similarity(user_preferences, item_vector)
        recommendations[item_name] = similarity
    sorted_recommendations = {k: v for k, v in sorted(recommendations.items(), key=lambda item: item[1], reverse=True)}
    return sorted_recommendations

# User preferences
user_preferences = [1, 0, 1, 0, 1]

# Get content-based recommendations
recommendations = content_based_recommendation(user_preferences, items)

# Print recommended items
print("Recommended items:")
for item_name, similarity in recommendations.items():
    print(f"{item_name} - Similarity: {similarity}")
