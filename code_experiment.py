
def recommend_movie():
    print("Welcome to the Movie Recommendation System!")
    genre = input("Please enter your preferred movie genre (e.g. comedy, action, horror): ")

    if genre.lower() == "comedy":
        print("We recommend you watch 'The Hangover'.")
    elif genre.lower() == "action":
        print("We recommend you watch 'The Avengers'.")
    elif genre.lower() == "horror":
        print("We recommend you watch 'The Conjuring'.")
    else:
        print("Sorry, we don't have a recommendation for that genre.")

recommend_movie()
