
import numpy as np

# Sample Data
user_preferences = {
    'user1': {
        'action': 5,
        'comedy': 2,
        'drama': 4,
        'romance': 1,
        'thriller': 3
    },
    'user2': {
        'action': 4,
        'comedy': 5,
        'drama': 2,
        'romance': 3,
        'thriller': 1
    },
    'user3': {
        'action': 2,
        'comedy': 3,
        'drama': 1,
        'romance': 5,
        'thriller': 4
    }
}

# Function to calculate similarity score using cosine similarity
def calculate_similarity_score(prefs, person1, person2):
    shared_items = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            shared_items[item] = 1

    if len(shared_items) == 0:
        return 0

    sum_of_products = sum([prefs[person1][item] * prefs[person2][item] for item in shared_items])
    sum_of_squares_person1 = sum([prefs[person1][item] ** 2 for item in prefs[person1]])
    sum_of_squares_person2 = sum([prefs[person2][item] ** 2 for item in prefs[person2]])

    similarity_score = sum_of_products / (np.sqrt(sum_of_squares_person1) * np.sqrt(sum_of_squares_person2))
    return similarity_score

# Function to recommend items to a given user
def recommend_items(prefs, person):
    similarity_scores = {}
    for other_person in prefs:
        if other_person != person:
            similarity_scores[other_person] = calculate_similarity_score(prefs, person, other_person)

    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    recommendations = {}
    for item in prefs[person]:
        if prefs[person][item] == 0:
            ratings = {other_person: prefs[other_person][item] for other_person in prefs if item in prefs[other_person] and prefs[other_person][item] > 0}
            if len(ratings) > 0:
                recommendations[item] = np.mean(list(ratings.values()))

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    return sorted_recommendations

# Main program starts here
target_user = 'user1'
recommended_items = recommend_items(user_preferences, target_user)

print("Recommended items for", target_user + ":")
for item, rating in recommended_items:
    print(item, "-", rating)
