
# Define a list of items with their corresponding features
items = {
    'movie1': ['action', 'thriller', 'fantasy'],
    'movie2': ['comedy', 'romance'],
    'book1': ['mystery', 'thriller', 'detective'],
    'book2': ['sci-fi', 'adventure']
}

# Define a function to calculate the similarity between two items based on their features
def similarity(item1, item2):
    features1 = set(items[item1])
    features2 = set(items[item2])
    intersection = features1.intersection(features2)
    return len(intersection) / (len(features1) + len(features2) - len(intersection))

# Define a function to recommend items based on a query item
def recommend(query_item):
    recommendations = {}
    for item in items:
        if item != query_item:
            recommendations[item] = similarity(query_item, item)
    # Sort recommendations by similarity in descending order
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Get user input for a query item
query_item = input("Enter a query item: ")

# Make recommendations based on the query item
recommendations = recommend(query_item)

# Display the top recommended items
print("Top recommendations for", query_item + ":")
for item, score in recommendations:
    print(item, "-", score)
