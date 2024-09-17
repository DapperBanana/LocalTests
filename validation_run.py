
# Sample content-based recommendation system
# Assume we have a database of items with features

# Create a dictionary of items with their features
items = {
    'item1': {
        'genre': 'action',
        'rating': 5
    },
    'item2': {
        'genre': 'comedy',
        'rating': 4
    },
    'item3': {
        'genre': 'drama',
        'rating': 3
    },
    'item4': {
        'genre': 'action',
        'rating': 4
    }
}

# Define a function to recommend items based on user input
def recommend_items(user_input, items):
    recommended_items = []
    
    # Iterate over the items and compare features with user input
    for item, features in items.items():
        if features['genre'] == user_input['genre'] and features['rating'] >= user_input['min_rating']:
            recommended_items.append(item)
    
    return recommended_items

# Get user input
user_input = {
    'genre': 'action',
    'min_rating': 4
}

# Get recommended items
recommended_items = recommend_items(user_input, items)

if recommended_items:
    print("Recommended items:", recommended_items)
else:
    print("No items found for the given input criteria.")
