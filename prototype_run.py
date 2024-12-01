

class ContentBasedRS:
    def __init__(self, items):
        self.items = items

    def get_recommendations(self, item):
        recommendations = []
        for other_item in self.items:
            if other_item != item:
                similarity = self.calculate_similarity(item, other_item)
                recommendations.append((other_item, similarity))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:5]

    def calculate_similarity(self, item1, item2):
        # This is a simple similarity calculation for demonstration purposes
        # In a real system, you would use more advanced techniques
        similarity = len(set(item1.split()) & set(item2.split()))
        return similarity

# Sample items
items = ["action movie", "comedy movie", "drama movie", "sci-fi movie", "horror movie"]

# Initialize the recommendation system with the items
rs = ContentBasedRS(items)

# Get recommendations for a specific item
item = "action movie"
recommendations = rs.get_recommendations(item)

print("Recommended items for", item + ": ")
for item, similarity in recommendations:
    print(item)

