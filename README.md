# SI_507_Final_Project
This project was created as a final project for SI 507 at the University of Michigan

# Instructions
PIP Installations: bs4, requests, webbrowser, json

To run this program, please download Python file "interaction_presentation.py", "read_Tree.py", and "tree_data.json". They should be placed within the same directory for the program to run properly. 

If you want to check other files, please feel to download all the other files you need. The "construct_tree.py" is used to construct the tree for storing all the data. During the constructing process, the "OMDb_Cache_final.json", "Box_Office_Cache.json", and "OMDb_Cache.json" are generated as caches.

The OMDb API needs API key and the process to supply API key is shown below:

First, set up a function to get data:

def get_OMDb_data(url, params=None):

    if params:
        return requests.get(url, params).json()
    else:
        return requests.get(url).json()


A 5-minute video of how the program runs can be found here: https://www.loom.com/share/1d8c3641e2804c26ba1c7efb2751e24d





