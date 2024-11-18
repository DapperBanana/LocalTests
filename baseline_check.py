
# Sample dataset of items with their attributes
items = {
    "item1": {"genre": "action", "rating": 4.5},
    "item2": {"genre": "horror", "rating": 3.0},
    "item3": {"genre": "comedy", "rating": 4.1},
    "item4": {"genre": "action", "rating": 4.8},
    "item5": {"genre": "comedy", "rating": 3.5}
}

# Function to recommend items based on genre
def recommend_items_by_genre(user_genre):
    recommended_items = []
    for item, attrs in items.items():
        if attrs["genre"] == user_genre:
            recommended_items.append(item)
    return recommended_items

# Function to recommend items based on rating
def recommend_items_by_rating(min_rating):
    recommended_items = []
    for item, attrs in items.items():
        if attrs["rating"] >= min_rating:
            recommended_items.append(item)
    return recommended_items

# Main function to recommend items based on user preferences
def recommend_items(user_genre, min_rating):
    genre_based_recommendations = recommend_items_by_genre(user_genre)
    rating_based_recommendations = recommend_items_by_rating(min_rating)
    
    recommended_items = list(set(genre_based_recommendations) & set(rating_based_recommendations))
    
    return recommended_items

# Test the recommendation system
user_genre = "action"
min_rating = 4.0
recommended_items = recommend_items(user_genre, min_rating)

print("Recommended items for the user:")
for item in recommended_items:
    print(item)
