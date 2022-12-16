# SI_507_Final_Project
This project was created as a final project for SI 507 at the University of Michigan

# Instructions
PIP Installations: bs4, requests, webbrowser, json

To run this program, please download Python file "interaction_presentation.py", "read_Tree.py", and "tree_data.json". They should be placed within the same directory for the program to run properly. 

If you want to check other files, please feel to download all the other files you need. The "construct_tree.py" is used to construct the tree for storing all the data. During the constructing process, the "OMDb_Cache_final.json", "Box_Office_Cache.json", and "OMDb_Cache.json" are generated as caches.

The OMDb API needs API key and the process to supply API key is shown below:
![image](https://user-images.githubusercontent.com/70920735/208057689-e53244c9-7fc4-427b-93b3-05fb124540d2.png)

# Interactions
This program has a variety of command line prompts. A 5-minute video of how the program runs can be found here: https://www.loom.com/share/1d8c3641e2804c26ba1c7efb2751e24d

To provide better recommendations, users will get 4 questions about genre, language, rating, and runtime to answer by entering the selections provided in the program. According to the answers, a list of movie recommendations will be displayed. The program will first show the basic information about the movies, such as title, year, genre, etc. Then, if the user wants to know more about a specific movie that the user is interested in, the user can enter the number of the movie in the list, and the more detailed information and the poster of the movie will be shown. If the user wants to know more about another movie, the user can enter the number of that movie as well. If the user wants to explore more types of movies, the previous 4 questions will show again and repeat the same process. Finally, if the user wants to exit, just need to enter ‘exit’.

# Data Structure
Description of the tree: The root node is a string: 'Movie Categorizer Starting Menu'. The level 1 consists of nodes representing genres, the level 2 consists of nodes representing languages, the level 3 consists of nodes representing ratings, the level 4 consists of nodes representing runtimes, and the level 5 consists of all the movies corresponding to their parent nodes.

How to organize the data into the tree: The tree is a set of lists [of lists [of lists …]]. There are two types of nodes. The first type is the internal node consisting of a string representing the name of the node as the first element in a list and the child nodes also in the list as the other elements. The second type is the leaf node consisting of the movies corresponding to the parent node. It doesn’t have any lists or child nodes connected to it.
