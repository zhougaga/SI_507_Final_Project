#
# Name: Jukai Zhou
#

import json


def readTree(tree_File_name, genre, language, rating, runtime):
    '''
    This function is used to read a json file of a tree and return the movies based on the information given by user.

    Parameters
    ----------
    tree_File_name: string
    genre: string
    language: string
    rating: string
    runtime: string

    Returns
    -------
    movies: list of dictionaries
    '''

    TREE_FILENAME = tree_File_name
    tree_file = open(TREE_FILENAME, 'r')
    tree_contents = tree_file.read()
    tree = json.loads(tree_contents)
    tree_file.close()

    returned_movies = []
    for g in tree[1:]:
        for l in g[1:]:
            for r in l[1:]:
                for run in r[1:]:
                    if len(run) > 1:
                        for movie in run[1:]:
                            if genre.lower() in movie['Genre'].lower():
                                if language.lower() in movie['Language'].lower():
                                    if float(movie['imdbRating']) >= float(rating.split(' - ')[0]) and float(movie['imdbRating']) <= float(rating.split(' - ')[1]):
                                        if movie['Runtime'][:2].isnumeric():
                                            if int(movie['Runtime'][:3]) >= int(runtime.split(' - ')[0]) and int(movie['Runtime'][:3]) <= int(runtime.split(' - ')[1]):
                                                if movie not in returned_movies:
                                                    returned_movies.append(movie)
                                        else:
                                            if int(movie['Runtime'][:2]) >= int(runtime.split(' - ')[0]) and int(movie['Runtime'][:2]) <= int(runtime.split(' - ')[1]):
                                                if movie not in returned_movies:
                                                    returned_movies.append(movie)

    return returned_movies
