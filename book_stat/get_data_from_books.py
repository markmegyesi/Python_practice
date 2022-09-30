

import collections
import re
import math
import json
import os
BOOKS_PATH = os.path.join(os.path.dirname(__file__),'books')
JSONS_PATH = os.path.join(os.path.dirname(__file__),'JSONs')

def get_books():
   return [item for item in os.listdir(BOOKS_PATH) if item.endswith('.txt')]

def read_and_json():
    for book in get_books():
        txt_file= os.path.join(BOOKS_PATH, book)
        if not os.path.exists(txt_file):
            raise Exception(f"Nem létezik az elérési útvonal: {txt_file}")
        with open(txt_file, "r", encoding="utf-8") as file:
            my_data = file.read()
        with open(f'book_stat\JSONs/{book}.json','w',encoding='utf-8') as json_file:
                json.dump(stats(my_data),json_file, indent=4)

     


def stats(my_data):
    stats={}
    def _page_num(stats):
        stats['oldalak_szama'] = math.ceil(len(my_data)/3000)
        return stats

    
    def _row_num(stats):
        row_counter = 0
        for row in my_data.split("\n"):
            row_counter+=1
        stats['sorok_szama']= row_counter
        return stats
    
    def _words(stats):
        word_counter = 0
        word_length = ""
        split_data = re.split(r'[^a-zA-Z]' , my_data)
        for word in split_data:
            if len(word) > 2:
                word_counter+=1
            
            if len(word) > len(word_length) :
                word_length = word
                stats['leghosszabb_szo'] = word
        stats['szavak_szama']=word_counter
        return stats
    def _author(stats):    
        author = re.search('Author:(.*)\n', my_data)
        stats['konyv_szerzoje']=author.group(1)
        return stats

    def _title(stats):
        title = re.search('Title:(.*)\n', my_data)
        stats['konyv_cime']=title.group(1)
        return stats

    def _release(stats):
        release = re.search('Release Date: (.*) \[EBook', my_data)
        if release != None:
            stats['kiadas_datuma']=release.group(1)
        else:
            release = re.search('Release Date:(.*)\n', my_data)
            if release != None:
                stats['kiadas_datuma']=release.group(1)
            else:
                release = re.search('Posting Date:(.*) \[EBook', my_data)
                stats['kiadas_datuma']=release.group(1)
        return stats

    def _top5_words(stats):
        Counter= collections.Counter(re.split(r'[^a-zA-Z]' , my_data))
        most_comm = Counter.most_common(15)
        most_occur={}
        for idx, item in enumerate(most_comm):
            if len(item[0])> 2:
                most_occur[item[0]]=item[1]
                if len(most_occur) == 5:
                    stats['leggyakoribb_szo'] = most_occur
                    break
        return stats

    _page_num(stats)
    _words(stats)
    _row_num(stats)
    _author(stats)
    _title(stats)
    _release(stats)
    _top5_words(stats)

    return stats

def get_jsons():
    return[item for item in os.listdir(JSONS_PATH) if item.endswith('.json')]
    
            
def min_max():
    max_counter=0
    min_counter=10000000000
    words_min=''
    words_max=''
    for jsons in get_jsons():
        json_file= os.path.join(JSONS_PATH, jsons)
        if not os.path.exists(json_file):
            raise Exception(f"Nem létezik az elérési útvonal: {json_file}")
        with open(json_file, "r", encoding="utf-8") as file:
            my_data = json.load(file)
        if my_data['szavak_szama'] > max_counter:
            max_counter = my_data['szavak_szama']
            words_max = my_data['konyv_cime']
        if my_data['szavak_szama'] < min_counter:
            min_counter = my_data['szavak_szama']
            words_min = my_data['konyv_cime']
        min_max_dict={
            'leghosszabb_konyv':words_max,
            'legrovidebb_konyv':words_min

        }
        with open('book_stat\JSONs/max_min.json','w',encoding='utf-8') as json_file:
                    json.dump(min_max_dict,json_file, indent=4)
        
def delete_the_shortest():
    with open("book_stat\JSONs\max_min.json", "r", encoding="utf-8") as file:
        my_data = json.load(file)
    shortest = my_data['legrovidebb_konyv']
    deleted_book = {
        'torolt_konyv':shortest
    }
    with open('book_stat\JSONs/deleted.json','w',encoding='utf-8') as json_file:
        json.dump(deleted_book,json_file, indent=4)
    
   
    os.remove(os.path.join(JSONS_PATH,(f"{shortest}.txt.json")))
    os.remove(os.path.join(JSONS_PATH,(f"book_stat\\books\{shortest}.txt")))
    



if __name__ == '__main__':
    
    read_and_json()
    min_max()
    delete_the_shortest()
    