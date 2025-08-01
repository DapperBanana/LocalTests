
# Recipe recommendation system

def recommend_recipe():
    print("Welcome to the recipe recommendation system!")
    print("What type of dish are you looking to make?")
    
    dish_type = input("Enter the type of dish (e.g. pasta, salad, dessert): ").lower()
    
    if dish_type == "pasta":
        print("Here is a recipe for pasta carbonara:")
        print("Ingredients:")
        print("- Spaghetti")
        print("- Eggs")
        print("- Parmesan cheese")
        print("- Pancetta or bacon")
        print("Instructions:")
        print("1. Cook the spaghetti according to package instructions.")
        print("2. Cook the pancetta or bacon in a pan until crispy.")
        print("3. In a bowl, whisk together eggs and Parmesan cheese.")
        print("4. Add the cooked spaghetti to the pan with the pancetta or bacon and toss to combine.")
        print("5. Remove from heat and stir in the egg mixture until creamy.")
        print("6. Serve and enjoy!")
    elif dish_type == "salad":
        print("Here is a recipe for a Caesar salad:")
        print("Ingredients:")
        print("- Romaine lettuce")
        print("- Croutons")
        print("- Parmesan cheese")
        print("- Caesar dressing")
        print("Instructions:")
        print("1. Wash and chop the romaine lettuce.")
        print("2. Add the croutons and Parmesan cheese to the lettuce.")
        print("3. Toss with Caesar dressing until well coated.")
        print("4. Serve and enjoy!")
    elif dish_type == "dessert":
        print("Here is a recipe for chocolate chip cookies:")
        print("Ingredients:")
        print("- Flour")
        print("- Butter")
        print("- Sugar")
        print("- Chocolate chips")
        print("Instructions:")
        print("1. Cream together butter and sugar.")
        print("2. Add flour and chocolate chips, mix until dough forms.")
        print("3. Roll dough into balls and place on baking sheet.")
        print("4. Bake at 350°F for 10-12 minutes.")
        print("5. Let cool and enjoy your cookies!")
    else:
        print("Sorry, we don't have a recipe for that dish type.")

# Call the recommend_recipe function
recommend_recipe()
