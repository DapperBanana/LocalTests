
# Sample dataset of user preferences
user_preferences = {
    "Alice": {"action": 5, "comedy": 3, "drama": 2, "horror": 1},
    "Bob": {"action": 2, "comedy": 4, "drama": 3, "horror": 5},
    "Charlie": {"action": 3, "comedy": 2, "drama": 4, "horror": 1},
    "David": {"action": 4, "comedy": 1, "drama": 5, "horror": 2}
}

# Function to calculate similarity between two users based on their preferences
def calculate_similarity(user1, user2):
    shared_preferences = {}
    for item in user_preferences[user1]:
        if item in user_preferences[user2]:
            shared_preferences[item] = 1

    if len(shared_preferences) == 0:
        return 0

    sum_of_squares = sum([pow(user_preferences[user1][item] - user_preferences[user2][item], 2) for item in shared_preferences])

    return 1 / (1 + sum_of_squares)

# Function to generate recommendations for a user
def get_recommendations(user):
    total_rated_scores = {}
    similarities = {}

    for other_user in user_preferences:
        if other_user == user:
            continue

        similarity = calculate_similarity(user, other_user)
        if similarity <= 0:
            continue

        for item in user_preferences[other_user]:
            if item not in user_preferences[user] or user_preferences[user][item] == 0:
                total_rated_scores.setdefault(item, 0)
                total_rated_scores[item] += user_preferences[other_user][item] * similarity
                similarities.setdefault(item, 0)
                similarities[item] += similarity

    recommendations = [(item, total_rated_scores[item] / similarities[item]) for item in total_rated_scores]
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations

# Sample usage
user = "Alice"
recommendations = get_recommendations(user)
print(f"Recommendations for {user}:")
for movie, score in recommendations:
    print(f"{movie}: {score}")
