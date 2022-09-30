


books_path = r"D:\Users\balihb\Desktop\Python (2)\db_book_stat\books"

db_params = {
    "user": "postgres",
    "password": "postgres",
    "db": "postgres",
    "host": "localhost",
    "port": 5432,
}

book_stat_insert=("""
insert into book_stat (
id ,
title,
num_of_pages,
longest_word,
num_of_words,
num_of_rows,
author,
release_date) values
(nextval('seq_book_stat'),%s,%s,%s,%s,%s,%s,%s)

""")



top_5_insert = ("""
insert into top5(
id,
title,
word,
word_length
)values
(nextval('seq_top5'),%s,%s,%s)
""")



min_max_insert = ("""
insert into min_max
(id,
max_title,
num_of_words_max,
min_title,
num_of_words_min) values 
(nextval('seq_min_max'),%s,%s,%s,%s)


""")

delete_shortest = ("delete from book_stat where title=%s")