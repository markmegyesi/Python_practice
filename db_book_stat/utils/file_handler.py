import collections
import re
import math
import json
import os

from params import books_path,book_stat_insert,top_5_insert,db_params,min_max_insert,delete_shortest
from db_handler import run_sql


def get_books(books_path):
   return [os.path.join(books_path,item) for item in os.listdir(books_path) if item.endswith('.txt')]

def get_data(file_loc):
    if not os.path.exists(file_loc):
        raise FileExistsError('A megadott file nem található!')
    with open (file_loc, "r",encoding="utf-8") as f:
        data = f.read()
    return data

def word_counter(data):
    return len([item for item in data.split(' ') if len(item) > 2])

def row_counter(data):
    return len(data.split('\n'))

def page_counter(data):
    return math.ceil(len(data)/3000)

def get_longestword(data):
    word_length = ""
    split_data = re.split(r'[^a-zA-Z]' , data)
    for word in split_data:
        if len(word) > len(word_length) :
            word_length = word
    return word_length    
    

def get_author(data):
    author = re.search('Author:(.*)\n', data)
    return (author.group(1))
    
def get_title(data):    
        author = re.search('Title:(.*)\n', data)
        return author.group(1)

def get_release(data):
    release = re.search('Release Date: (.*) \[EBook', data)
    if release != None:
        release = release.group(1)
    else:
        release = re.search('Release Date:(.*)\n', data)
        if release != None:
            release = release.group(1)
        else:
            release = re.search('Posting Date:(.*) \[EBook', data)
            release = release.group(1)
    return release

def top5_words(data):
    Counter= collections.Counter(re.split(r'[^a-zA-Z]' , data))
    most_comm = Counter.most_common(15)
    most_occur={}
    for idx, item in enumerate(most_comm):
        if len(item[0])> 2:
            most_occur[item[0]]=item[1]
            if len(most_occur) == 5:
                return most_occur

def delete_the_shortest (title):
    run_sql(db_params,delete_shortest,title)


def etl():
    stats = {}
    max_counter=0
    min_counter=10000000000
    words_min=''
    words_max=''
    for idx, item in enumerate(get_books(books_path)):
        data = get_data(item)
        stats ['title'] = get_title(data)
        stats ['num_of_pages'] = page_counter(data)
        stats ['longest_word'] = get_longestword(data)
        stats ['num of words'] = word_counter (data)
        stats ['num of rows'] = row_counter(data) 
        stats ['author'] = get_author(data)
        stats ['release_date'] = get_release(data)
        top5=top5_words(data)
       
       
        run_sql(db_params,book_stat_insert,tuple(stats.values()+stats['title']))
        for key, value in top5.items():
            my_list=[stats['title'],stats['title'],key,value]
            run_sql(db_params,top_5_insert,tuple(my_list))
    
        
        
        if max_counter < stats ['num of words']:
            words_max = stats ['title']
            max_counter = stats['num of words']
        if min_counter > stats['num of words']:
            words_min = stats['title']
            min_counter = stats['num of rows']
    min_max_params=(words_max,max_counter,words_min,min_counter)
    run_sql(db_params,min_max_insert,min_max_params)
    delete_the_shortest(words_min)

if __name__=='__main__':
    from params import books_path,book_stat_insert,top_5_insert,db_params,min_max_insert,delete_shortest
    from db_handler import run_sql
    most_occur={}
    stats = {}
    max_counter=0
    min_counter=10000000000
    words_min=''
    words_max=''
    for idx, item in enumerate(get_books(books_path)):
        data = get_data(item)
        stats ['title'] = get_title(data)
        stats ['num_of_pages'] = page_counter(data)
        stats ['longest_word'] = get_longestword(data)
        stats ['num of words'] = word_counter (data)
        stats ['num of rows'] = row_counter(data) 
        stats ['author'] = get_author(data)
        stats ['release_date'] = get_release(data)
        top5=top5_words(data)
        run_sql(db_params,book_stat_insert,tuple(stats.values()))
        for key, value in top5.items():
            my_list=[stats['title'],key,value]
            run_sql(db_params,top_5_insert,tuple(my_list))
        
        if max_counter < stats ['num of words']:
            words_max = stats ['title']
            max_counter = stats['num of words']
        if min_counter > stats['num of words']:
            words_min = stats['title']
            min_counter = stats['num of words']
    min_max_params=(words_max,max_counter,words_min,min_counter)
    run_sql(db_params,min_max_insert,min_max_params)
    delete_the_shortest(list(words_min))
