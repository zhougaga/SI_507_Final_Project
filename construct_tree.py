#
# Name: Jukai Zhou
#

import requests
from bs4 import BeautifulSoup
import json

### Scraping for box office of movies ###
box_office_url = 'https://www.boxofficemojo.com/year/world/'
years = ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']

def scrape_data(url, year):
    '''
    This function is used to scrape data from the website which contains the information top 200 (box office) movies in a specific year,
    then summarize the information into a dictionary and return it.

    Parameters
    ----------
    url: string (this is for scraping)
    year: string (this is used to complete the url with a specific year)

    Returns
    -------
    scraped_data_dic: dictionary (includes the information about top 200 (box office) movies in a specific year)
    '''

    new_url = url + year
    page = requests.get(new_url)
    soup = BeautifulSoup(page.text, 'lxml')

    table1 = soup.find('div', id='table')

    scraped_data_dic = {}
    scraped_data_dic[year] = []
    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        table_data_dic = {}
        table_data_dic['Rank'] = row[0]
        table_data_dic['Title'] = row[1]
        table_data_dic['Worldwide_Box_Office'] = row[2]
        table_data_dic['Domestic_Box_Office'] = row[3]
        table_data_dic['Domestic_Box_Office_Percentage'] = row[4]
        table_data_dic['Foreign_Box_Office'] = row[5]
        table_data_dic['Foreign_Box_Office_Percentage'] = row[6]
        scraped_data_dic[year].append(table_data_dic)

    return scraped_data_dic

# The code between ''' and ''' here is used to save data from scraping in cache. Putting them in ''' and ''' is to avoid scraping again and wasting time #
# If you want to run the code below, you can delete the ''' and ''' #
'''
box_office_cache = {}
for year in years:
    box_office_cache[year] = scrape_data(box_office_url, year)[year]

CACHE_FILENAME_1 = 'Box_Office_Cache.json'
dumped_json_cache = json.dumps(box_office_cache)
save_cache = open(CACHE_FILENAME_1, "w")
save_cache.write(dumped_json_cache)
save_cache.close()
'''
CACHE_FILENAME_1 = 'Box_Office_Cache.json'


### Get data from OMDb API and combine them with data from scraping ###

def get_OMDb_data(url, params=None):
    '''
    This function is used to get data from OMDb API with the url and parameters that are used to complete the url,
    then convert the json file into dictionary and return it.

    Parameters
    ----------
    url: string
    params: dictionary

    Returns
    -------
    requests.get(url, params).json(): dictionary
    requests.get(url).json(): dictionary
    '''

    if params:
        return requests.get(url, params).json()
    else:
        return requests.get(url).json()

OMDb_url = "http://www.omdbapi.com/?apikey=70ab3d7a"

cache_file = open(CACHE_FILENAME_1, 'r')
cache_contents = cache_file.read()
cache_dict = json.loads(cache_contents)
cache_file.close()
#print(len(cache_dict['2020']))

# Below is used to get data from OMDb API and combine the data with the data from scraping #
# Putting them in ''' and ''' is to avoid retrieving data again and wasting time #
# If you want to run the code below, you can delete the ''' and ''' #
'''
CACHE_FILENAME_2 = 'OMDb_Cache.json'
cache_file_2 = open(CACHE_FILENAME_2, 'r')
cache_contents_2 = cache_file_2.read()
cache_dict_2 = json.loads(cache_contents_2)
cache_file_2.close()

#combine_OMDb_box_office = {}
for year in years[5:]:
    cache_dict_2[year] = []
    for movie in cache_dict[year]:
        params = {'t': movie['Title'], 'y': year}
        result = get_OMDb_data(OMDb_url, params)

        if 'Title' in result.keys():
            result['Rank'] = movie['Rank']
            result['Worldwide_Box_Office'] = movie['Worldwide_Box_Office']
            result['Domestic_Box_Office'] = movie['Domestic_Box_Office']
            result['Domestic_Box_Office_Percentage'] = movie['Domestic_Box_Office_Percentage']
            result['Foreign_Box_Office'] = movie['Foreign_Box_Office']
            result['Foreign_Box_Office_Percentage'] = movie['Foreign_Box_Office_Percentage']
            cache_dict_2[year].append(result)

CACHE_FILENAME_3 = 'OMDb_Cache_final.json'
dumped_json_cache_3 = json.dumps(cache_dict_2)
save_cache_3 = open(CACHE_FILENAME_3, "w")
save_cache_3.write(dumped_json_cache_3)
save_cache_3.close()
'''


CACHE_FILENAME_4 = 'OMDb_Cache_final.json'
cache_file_4 = open(CACHE_FILENAME_4, 'r')
cache_contents_4 = cache_file_4.read()
cache_dict_4 = json.loads(cache_contents_4)
cache_file_4.close()

#print(len(cache_dict_2['2022']))


### Construct tree to store the data ###

data_tree = []

tree_root = 'Movie Categorizer Starting Menu'
data_tree.append(tree_root)

genre = ['Action', 'Animation', 'Adventure', 'Biography', 'Drama', 'Comedy', 'Romance', 'Sci-Fi', 'Thriller', 'Family', 'Crime', 'Sport', 'Mystery', 'Fantasy', 'Music', 'History']
for g in genre:
    data_tree.append([g])

language = ['English', 'Russian', 'Korean', 'Italian', 'Mandarin', 'Malay', 'French', 'Spanish', 'Japanese', 'Arabic', 'Thai', 'German']
for g in data_tree[1:]:
    for l in language:
        g.append([l])

rating = ['8.0 - 10.0', '7.0 - 8.0', '6.0 - 7.0', '5.0 - 6.0', '0.0 - 5.0']
for g in data_tree[1:]:
    for l in g[1:]:
        for r in rating:
            l.append([r])

runtime = ['150 - 999', '120 - 150', '90 - 120', '60 - 90', '0 - 60']
for g in data_tree[1:]:
    for l in g[1:]:
        for r in l[1:]:
            for run in runtime:
                r.append([run])


for g in data_tree[1:]:
    for l in g[1:]:
        for r in l[1:]:
            for run in r[1:]:
                for year in cache_dict_4.keys():
                    for movie in cache_dict_4[year]:
                        if g[0] in movie['Genre']:
                            if l[0] in movie['Language']:
                                if 'N/A' not in movie['imdbRating']:
                                    if float(movie['imdbRating']) >= float(r[0].split(' - ')[0]) and float(movie['imdbRating']) <= float(r[0].split(' - ')[1]):
                                        if 'N/' not in movie['Runtime']:
                                            if movie['Runtime'][:2].isnumeric():
                                                if int(movie['Runtime'][:3]) >= int(run[0].split(' - ')[0]) and int(movie['Runtime'][:3]) <= int(run[0].split(' - ')[1]):
                                                    run.append(movie)
                                            else:
                                                if int(movie['Runtime'][:2]) >= int(run[0].split(' - ')[0]) and int(movie['Runtime'][:2]) <= int(run[0].split(' - ')[1]):
                                                    run.append(movie)


CACHE_FILENAME_5 = 'tree_data.json'
dumped_json_cache_5 = json.dumps(data_tree)
save_cache_5 = open(CACHE_FILENAME_5, "w")
save_cache_5.write(dumped_json_cache_5)
save_cache_5.close()

