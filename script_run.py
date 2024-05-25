
# Define a dictionary of items with their attributes
items = {
    "item1": {
        "genre": "action",
        "rating": 4
    },
    "item2": {
        "genre": "comedy",
        "rating": 3
    },
    "item3": {
        "genre": "drama",
        "rating": 5
    },
    "item4": {
        "genre": "action",
        "rating": 5
    },
    "item5": {
        "genre": "comedy",
        "rating": 2
    }
}

# Get user input for their preferences
user_genre = input("Enter your preferred genre (action, comedy, drama): ")
user_rating = int(input("Enter your preferred minimum rating (1-5): "))

# Find items that match user preferences
recommended_items = []
for item in items:
    if items[item]["genre"] == user_genre and items[item]["rating"] >= user_rating:
        recommended_items.append(item)

# Display recommended items
if recommended_items:
    print("Recommended items:")
    for item in recommended_items:
        print(item)
else:
    print("No items found matching your preferences.")
