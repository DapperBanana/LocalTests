
recipes = {
    "pasta": ["spaghetti", "tomato sauce", "parmesan cheese"],
    "salad": ["lettuce", "tomato", "cucumber", "dressing"],
    "sandwich": ["bread", "meat", "cheese", "lettuce", "tomato", "mayo"]
}

def recommend_recipe():
    print("Welcome to the recipe recommendation system!")
    print("Here are the available recipes:")
    for recipe in recipes:
        print("- " + recipe)
    
    user_choice = input("Enter the name of a recipe you would like to make: ")
    
    if user_choice in recipes:
        print("Great choice! Here is the list of ingredients you will need:")
        for ingredient in recipes[user_choice]:
            print("- " + ingredient)
    else:
        print("Sorry, that recipe is not available. Please choose another recipe.")

recommend_recipe()
