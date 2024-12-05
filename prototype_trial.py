
# Define some sample user data
user_data = {
    "Alice": {"action", "comedy", "drama"},
    "Bob": {"comedy", "romance"},
    "Charlie": {"action", "romance", "sci-fi"},
    "David": {"horror", "thriller", "sci-fi"}
}

# Define some sample items and their genres
item_data = {
    "Movie1": {"action", "drama"},
    "Movie2": {"comedy", "romance"},
    "Movie3": {"action", "sci-fi"},
    "Movie4": {"horror", "thriller"},
    "Movie5": {"comedy", "drama"}
}

# Function to get recommendations for a user
def get_recommendations(user):
    user_genres = user_data.get(user, {})
    recommendations = {}
    
    for item, genres in item_data.items():
        score = 0
        for genre in genres:
            if genre in user_genres:
                score += 1
        
        recommendations[item] = score
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recommendations

# Get recommendations for user Alice
recommendations = get_recommendations("Alice")

# Print recommendations
print("Recommendations for Alice:")
for item, score in recommendations:
    print(f"- {item} (score: {score})")
