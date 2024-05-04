
# Sample dataset of items with features
items = {
    'item1': {'genre': 'action', 'language': 'english', 'rating': 4.5},
    'item2': {'genre': 'comedy', 'language': 'english', 'rating': 3.5},
    'item3': {'genre': 'drama', 'language': 'spanish', 'rating': 4.0},
    'item4': {'genre': 'action', 'language': 'english', 'rating': 4.0},
    'item5': {'genre': 'comedy', 'language': 'spanish', 'rating': 3.0},
}

# Function to recommend items based on user preferences
def content_based_recommendation(user_preferences):
    recommended_items = []
    
    for item in items:
        match_score = 0
        
        for feature, value in user_preferences.items():
            if items[item].get(feature) == value:
                match_score += 1
        
        if match_score == len(user_preferences):
            recommended_items.append(item)
    
    return recommended_items

# Test the recommendation system
user_preferences = {'genre': 'action', 'language': 'english'}
recommendations = content_based_recommendation(user_preferences)

print("Recommended items based on user preferences:")
for item in recommendations:
    print(f"- {item}")
