from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

def count_words(text):
    """
    Count the number of timeseach word occurs in text (str).
    Returns a dictionary where keys are unique words and values are word counts. Skip punctuation
    """
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"','{','}',"[", ']', "(", ")", '?', "-", '!']
    for ch in skips:
        text = text.replace(ch, '')
    word_counts = {}
    for word in text.split(' '):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words_fast(text):
    """
    Count the number of timeseach word occurs in text (str).
    Returns a dictionary where keys are unique words and values are word counts. Skip punctuation
    """
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"','{','}',"[", ']', "(", ")", '?',"-", "!"]
    for ch in skips:
        text = text.replace(ch, '')
    word_counts =Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, 'r', encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace('\n','').replace('\r','')
    return text

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

book_dir = "C:/Users/manis/Desktop/Study Material/Language Processing/Books"
stats = pd.DataFrame(columns = ('language','author','title','length', 'unique'))
title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir +"/"+ language):
        for title in os.listdir(book_dir +"/"+ language +"/"+ author):
            inputfile = book_dir +"/"+ language +"/"+ author +"/"+ title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title, sum(counts), num_unique
            title_num += 1
            
print(stats)

plt.figure(figsize = (10,10))
subset = stats[stats.language=='English']
plt.loglog(subset.length, subset.unique, 'o', label="$English$", color="crimson")
subset = stats[stats.language=='German']
plt.loglog(subset.length, subset.unique, 'o', label="$German$", color="forestgreen")
subset = stats[stats.language=='French']
plt.loglog(subset.length, subset.unique, 'o', label="$English$", color="orange")
subset = stats[stats.language=='Portuguese']
plt.loglog(subset.length, subset.unique, 'o', label="$Portuguese$", color="blueviolet")
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.legend()
plt.show()    
