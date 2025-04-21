
# Sample items and user preferences
items = {
    "item1": {"genre": "action", "rating": 4.5},
    "item2": {"genre": "comedy", "rating": 3.0},
    "item3": {"genre": "drama", "rating": 5.0},
    "item4": {"genre": "action", "rating": 4.0},
    "item5": {"genre": "comedy", "rating": 3.5},
}

user_preferences = {
    "action": 5.0,
    "comedy": 4.0,
    "drama": 3.0
}

# Content-based recommendation system
def content_based_recommender(user_prefs, items):
    recommendations = {}
    
    for item_id, item_info in items.items():
        sim_score = 0
        for genre, rating in user_prefs.items():
            if genre in item_info["genre"]:
                sim_score += rating
        
        recommendations[item_id] = sim_score
        
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Get recommendations for the user based on their preferences
recommended_items = content_based_recommender(user_preferences, items)

# Print out the recommended items
print("Recommended items:")
for item_id, score in recommended_items:
    print(f"{item_id}: {items[item_id]} (Score: {score})")
