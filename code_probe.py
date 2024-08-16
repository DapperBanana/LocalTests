
def movie_recommendation():
    print("Welcome to the Movie Recommendation System")
    print("Choose a genre to get a recommendation:")
    print("1. Action")
    print("2. Comedy")
    print("3. Drama")
    
    user_choice = input("Enter a number corresponding to the genre: ")

    if user_choice == "1":
        print("I recommend watching 'Mad Max: Fury Road'")
    elif user_choice == "2":
        print("I recommend watching 'The Grand Budapest Hotel'")
    elif user_choice == "3":
        print("I recommend watching 'The Shawshank Redemption'")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

movie_recommendation()
