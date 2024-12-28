
import numpy as np

# Define sample data of items and their features
items = {
    "item1": {"feature1": 1, "feature2": 0, "feature3": 1},
    "item2": {"feature1": 0, "feature2": 1, "feature3": 0},
    "item3": {"feature1": 1, "feature2": 1, "feature3": 0},
    "item4": {"feature1": 0, "feature2": 1, "feature3": 1}
}

# Function to calculate similarity between items based on their features
def cosine_similarity(item1, item2):
    item1_features = np.array(list(item1.values()))
    item2_features = np.array(list(item2.values()))
    
    dot_product = np.dot(item1_features, item2_features)
    norm_item1 = np.linalg.norm(item1_features)
    norm_item2 = np.linalg.norm(item2_features)
    
    similarity = dot_product / (norm_item1 * norm_item2)
    
    return similarity

# Function to recommend items based on user's preferences
def content_based_recommendation(user_preferences, items, n=3):
    recommendations = {}
    
    for item in items:
        sim = cosine_similarity(user_preferences, items[item])
        recommendations[item] = sim
        
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recommendations[:n]

# User preferences for features
user_preferences = {"feature1": 1, "feature2": 0, "feature3": 1}

# Get recommendations for user
recommendations = content_based_recommendation(user_preferences, items, n=2)

print("Recommended items:")
for item, similarity in recommendations:
    print(item, "with similarity score:", similarity)
