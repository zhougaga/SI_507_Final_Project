#
# Name: Jukai Zhou
#


from read_Tree import readTree
import webbrowser


def main():
    '''
    This function is used to interact with users and provide the movie recommendations based on the answers
    provided by the users.
    '''


    filename = 'tree_data.json'

    while True:

        print("\nWelcome to Movie Recommender!")
        print("We have 2000 movies in our database!")
        print("It includes top 200 most popular movies of each year in the last 10 years!\n")

        print("We will have 4 questions for you to help provide the best recommendations.\n")

        print("Question 1 is about Genre: Which genre do you prefer?")
        print("Please choose one from the followings:")
        print('Action   Animation   Adventure   Biography   Drama   Comedy   Romance   Sci-Fi   Thriller   Family   Crime   Sport   Mystery   Fantasy   Music   History')
        genre = input('Please enter here: ')

        print("\nQuestion 2 is about Language: Which language do you perfer?")
        print("Please choose one from the followings:")
        print('English   Russian   Korean   Italian   Mandarin   Malay   French   Spanish   Japanese   Arabic   Thai   German')
        language = input('Please enter here: ')

        print("\nQuestion 3 is about Rating: Which rating range do you prefer?")
        print("Please choose one from the followings:")
        print('8.0 - 10.0    7.0 - 8.0    6.0 - 7.0    5.0 - 6.0    0.0 - 5.0')
        rating = input('Please enter here (please enter the exact same format as the ones shown above): ')

        print("\nQuestion 4 is about Runtime: Which runtime range (min) do you prefer?")
        print("Please choose one from the followings:")
        print('150 - 999    120 - 150    90 - 120    60 - 90    0 - 60')
        runtime = input('Please enter here (please enter the exact same format as the ones shown above): ')

        results = readTree(filename, genre, language, rating, runtime)
        
        if results == []:
                continue_or_not = input("\nSorry, there are no results based on your preference. Do you want to try again? (please enter yes/no) ")
                if continue_or_not.lower() == 'yes':
                    print("\nThank you for giving another opportunity! Let's do it again!")
                elif continue_or_not.lower() == 'no':
                    break

        else:
            print('\nMovie Recommendations:')
            
            indx = 0
            for movie in results:
                indx += 1
                print(f"{indx}", showMovie(movie))

            break

    while True:
        print("\nIf you want to exit, please enter 'exit' below.")
        next_step = input("Enter a number for more info, or 'another' for another recommendation, or exit: ")

        if next_step.isnumeric():
            if int(next_step) <= indx and int(next_step) >= 1:
                print(showDetails(results[int(next_step)-1]))
                webbrowser.open(results[int(next_step)-1]['Poster'])
            else:
                next_step_again = input(f"Please enter an integer between 1 and {indx} as a choice: ")
                print(showDetails(results[int(next_step_again)-1]))
                webbrowser.open(results[int(next_step_again)-1]['Poster'])

        elif next_step.lower() == 'exit':
            print("\nThank you for using Movie Recommender!")
            print("\nBye!")
            break

        elif next_step.lower() == 'another':
            print("\nWe will have 4 questions for you to help provide the best recommendations.\n")

            print("Question 1 is about Genre: Which genre do you prefer?")
            print("Please choose one from the followings:")
            print('Action   Animation   Adventure   Biography   Drama   Comedy   Romance   Sci-Fi   Thriller   Family   Crime   Sport   Mystery   Fantasy   Music   History')
            genre = input('Please enter here: ')

            print("\nQuestion 2 is about Language: Which language do you perfer?")
            print("Please choose one from the followings:")
            print('English   Russian   Korean   Italian   Mandarin   Malay   French   Spanish   Japanese   Arabic   Thai   German')
            language = input('Please enter here: ')

            print("\nQuestion 3 is about Rating: Which rating range do you prefer?")
            print("Please choose one from the followings:")
            print('8.0 - 10.0    7.0 - 8.0    6.0 - 7.0    5.0 - 6.0    0.0 - 5.0')
            rating = input('Please enter here (please enter the exact same format as the ones shown above): ')

            print("\nQuestion 4 is about Runtime: Which runtime range (min) do you prefer?")
            print("Please choose one from the followings:")
            print('150 - 999    120 - 150    90 - 120    60 - 90    0 - 60')
            runtime = input('Please enter here (please enter the exact same format as the ones shown above): ')

            results = readTree(filename, genre, language, rating, runtime)
            if results == []:
                continue_or_not = input("\nSorry, there are no results based on your preference. Do you want to try again? (please enter yes/no) ")
                if continue_or_not.lower() == 'yes':
                    print("\nThank you for giving another opportunity! Let's do it again!")
                elif continue_or_not.lower() == 'no':
                    print('\nBye!')
                    break
            
            else:
                print('\nMovie Recommendations:')
                
                indx = 0
                for movie in results:
                    indx += 1
                    print(f"{indx}", showMovie(movie))


def showMovie(movie):
    '''
    This funtion is used to show the basic information about movies.

    Parameters
    ----------
    movie: dictionary

    Returns
    -------
    movie_info: string
    '''

    movie_info = f"Title: {movie['Title']} | Year: {movie['Year']} | Genre: {movie['Genre']} | Runtime: {movie['Runtime']} | Rating: {movie['imdbRating']} | Language: {movie['Language']}"
    return movie_info

def showDetails(movie):
    '''
    This function is used to show detailed information about movies.

    Parameters
    ----------
    movie: dictionary

    Returns
    -------
    details: string
    '''

    details = f"Title: {movie['Title']} | Year: {movie['Year']} | Genre: {movie['Genre']} | Runtime: {movie['Runtime']} | Rating: {movie['imdbRating']} | Language: {movie['Language']}\nPlot: {movie['Plot']}\nDirector: {movie['Director']}\nActors: {movie['Actors']}\nBox Office Rank in {movie['Year']}: {movie['Rank']}\nWorldwide Box Office: {movie['Worldwide_Box_Office']}\nAwards: {movie['Awards']}\nCountry: {movie['Country']}\n"
    return details


if __name__ == "__main__":
    main()
