
# Recipe recommendation system

recipes = {
    "spaghetti": ["spaghetti", "tomato sauce", "meatballs", "parmesan cheese"],
    "chicken curry": ["chicken", "curry paste", "coconut milk", "rice"],
    "stir-fry vegetables": ["mixed vegetables", "soy sauce", "garlic", "ginger"],
    "banana bread": ["bananas", "flour", "sugar", "eggs"]
}

def recommend_recipe(ingredients):
    recommended_recipe = None
    max_overlap = 0
    
    for recipe, recipe_ingredients in recipes.items():
        overlap = len(set(ingredients) & set(recipe_ingredients))
        if overlap > max_overlap:
            max_overlap = overlap
            recommended_recipe = recipe
    
    return recommended_recipe

def main():
    user_input = input("Enter ingredients separated by commas: ").lower()
    user_ingredients = user_input.split(", ")
    
    recommended_recipe = recommend_recipe(user_ingredients)
    
    if recommended_recipe:
        print(f"We recommend making {recommended_recipe} with the ingredients you have.")
    else:
        print("Sorry, we couldn't find a recipe that matches your ingredients.")
    
if __name__ == "__main__":
    main()
