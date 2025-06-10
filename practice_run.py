
# Sample items and their features
items = {
    "movie1": ["action", "adventure", "sci-fi"],
    "movie2": ["comedy", "romance"],
    "movie3": ["drama", "romance"],
    "book1": ["mystery", "thriller", "crime"],
    "book2": ["fantasy", "adventure"],
    "book3": ["romance", "drama"]
}

# User input
user_input = ["action", "sci-fi"]

# Calculate similarity between items and user input
similarities = {}
for item, features in items.items():
    intersection = set(features) & set(user_input)
    similarity_score = len(intersection) / len(user_input)
    similarities[item] = similarity_score

# Sort items based on similarity score
recommendations = sorted(similarities, key=similarities.get, reverse=True)

# Print recommendations
print("Recommended items based on your preferences:")
for i in range(min(3, len(recommendations))):
    print(recommendations[i])
