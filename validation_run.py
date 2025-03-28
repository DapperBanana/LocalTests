
def movie_recommendation():
    print("Welcome to the Movie Recommendation System!")
    print("Please answer a few questions so we can recommend a movie for you.")

    genre = input("What genre of movie do you prefer? (Action, Comedy, Drama, Horror, Sci-Fi): ").lower()
    mood = input("What mood are you in? (Happy, Sad, Scared, Excited): ").lower()

    if genre == "action" and mood == "excited":
        print("We recommend: The Avengers")
    elif genre == "comedy" and mood == "happy":
        print("We recommend: The Hangover")
    elif genre == "drama" and mood == "sad":
        print("We recommend: The Fault in Our Stars")
    elif genre == "horror" and mood == "scared":
        print("We recommend: Paranormal Activity")
    elif genre == "sci-fi":
        print("We recommend: Interstellar")
    else:
        print("Sorry, we don't have a recommendation for that combination.")

movie_recommendation()
