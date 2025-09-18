
# Sample data of items and their features
items = {
    'item1': ['action', 'comedy'],
    'item2': ['drama', 'romance'],
    'item3': ['action', 'adventure'],
    'item4': ['comedy', 'romance'],
    'item5': ['drama', 'thriller']
}

# Function to recommend items based on user preferences
def recommend_items(preferences):
    recommended_items = {}
    for item, features in items.items():
        similarity_score = 0
        for pref in preferences:
            if pref in features:
                similarity_score += 1
        recommended_items[item] = similarity_score
    recommended_items = dict(sorted(recommended_items.items(), key=lambda x: x[1], reverse=True))
    return recommended_items

# Get user preferences
user_preferences = input("Enter your preferences (separated by comma): ").split(',')

# Get recommended items
recommended_items = recommend_items(user_preferences)
print("Recommended items:")
for item, score in recommended_items.items():
    print(f"{item}: {score} matches")
