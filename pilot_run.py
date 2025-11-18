
# Sample dataset of user preferences for different items
user_preferences = {
    'Alice': {'movie': 4, 'music': 5, 'book': 3},
    'Bob': {'movie': 2, 'music': 4, 'book': 5},
    'Charlie': {'movie': 5, 'music': 3, 'book': 4}
}

# Function to calculate similarity between two users based on their preferences
def calculate_similarity(user1, user2):
    shared_items = set(user1.keys()) & set(user2.keys())
    
    numerator = sum(user1[item] * user2[item] for item in shared_items)
    denominator = (sum(user1[item] ** 2 for item in user1) ** 0.5) * (sum(user2[item] ** 2 for item in user2) ** 0.5)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

# Function to recommend items to a target user based on their preferences and other users' preferences
def content_based_recommendation(target_user, all_users):
    similarities = {}
    
    for user in all_users:
        if user != target_user:
            similarity = calculate_similarity(all_users[target_user], all_users[user])
            similarities[user] = similarity
            
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    
    recommended_items = {}
    for item in all_users[target_user]:
        if all_users[target_user][item] <= 3:
            for user, _ in sorted_similarities:
                if all_users[user][item] > 3:
                    recommended_items[item] = all_users[user][item]
                    break
    
    return recommended_items

# Sample target user
target_user = 'Alice'

# Generate recommendations for the target user
recommendations = content_based_recommendation(target_user, user_preferences)

print(f"Recommendations for {target_user}: {recommendations}")
