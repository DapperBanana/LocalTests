
# Movie recommendation system

def recommend_movie():
    print("Welcome to the movie recommendation system!")
    genre = input("What genre are you in the mood for? (action, comedy, drama, horror, sci-fi): ")
    
    if genre == "action":
        print("I recommend watching: The Dark Knight")
    elif genre == "comedy":
        print("I recommend watching: Superbad")
    elif genre == "drama":
        print("I recommend watching: The Shawshank Redemption")
    elif genre == "horror":
        print("I recommend watching: The Conjuring")
    elif genre == "sci-fi":
        print("I recommend watching: Blade Runner 2049")
    else:
        print("Sorry, I don't have any recommendations for that genre.")
    
    another_recommendation = input("Would you like another recommendation? (yes/no): ")
    
    if another_recommendation == "yes":
        recommend_movie()
    else:
        print("Enjoy your movie!")
        

recommend_movie()
