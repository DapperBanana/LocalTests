
# Dictionary of items with their respective features
items = {
    "item1": ["action", "adventure"],
    "item2": ["comedy", "romance"],
    "item3": ["horror"],
    "item4": ["action", "comedy"]
}

# Function to calculate similarity between items
def calculate_similarity(item1, item2):
    common_features = set(items[item1]).intersection(set(items[item2]))
    similarity_score = len(common_features) / len(items[item1])
    return similarity_score

# Function to recommend items based on user preferences
def recommend_items(preferences):
    recommended_items = {}
    for item in items:
        if item not in preferences:
            similarity_score = 0
            for preference in preferences:
                similarity_score += calculate_similarity(item, preference)
            recommended_items[item] = similarity_score
    sorted_items = sorted(recommended_items.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items]

# User preferences
user_preferences = ["action", "adventure"]

# Get recommended items based on user preferences
recommended_items = recommend_items(user_preferences)
print("Recommended items based on user preferences:")
for item in recommended_items:
    print(item)
