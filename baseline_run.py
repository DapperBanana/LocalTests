
import random

recipes = {
    "Pasta": ["Spaghetti Aglio e Olio", "Penne Arrabbiata", "Creamy Garlic Parmesan Pasta"],
    "Pizza": ["Margherita Pizza", "Pepperoni Pizza", "Vegetable Pizza"],
    "Salad": ["Caesar Salad", "Greek Salad", "Caprese Salad"],
    "Soup": ["Tomato Soup", "Chicken Noodle Soup", "Vegetable Soup"]
}

def recommend_recipe():
    print("Welcome to the Recipe Recommendation System!")
    print("Please select a type of cuisine: ")
    print("1. Pasta")
    print("2. Pizza")
    print("3. Salad")
    print("4. Soup")
    user_choice = input("Enter the number corresponding to your choice: ")

    if user_choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
    else:
        cuisine = get_cuisine(user_choice)
        recommend = get_recommendation(cuisine)
        print(f"I recommend trying the following {cuisine} recipe: {recommend}")

def get_cuisine(choice):
    if choice == "1":
        return "Pasta"
    elif choice == "2":
        return "Pizza"
    elif choice == "3":
        return "Salad"
    elif choice == "4":
        return "Soup"

def get_recommendation(cuisine):
    return random.choice(recipes[cuisine])

recommend_recipe()
