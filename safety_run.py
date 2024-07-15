
class ContentBasedRecommender:
    def __init__(self):
        self.item_profiles = {
            'item1': {'genre': 'action', 'year': 2010},
            'item2': {'genre': 'comedy', 'year': 2015},
            'item3': {'genre': 'action', 'year': 2018},
            'item4': {'genre': 'drama', 'year': 2012},
            'item5': {'genre': 'comedy', 'year': 2017},
        }

    def get_recommendations(self, user_profile):
        recommended_items = []
        
        for item, profile in self.item_profiles.items():
            if profile['genre'] == user_profile['genre'] and abs(profile['year'] - user_profile['year']) <= 5:
                recommended_items.append(item)
        
        return recommended_items

# Sample user profile
user_profile = {'genre': 'action', 'year': 2015}

# Initialize the recommender system
recommender = ContentBasedRecommender()

# Get recommendations based on user profile
recommendations = recommender.get_recommendations(user_profile)

print("Recommended items:")
for item in recommendations:
    print(item)
