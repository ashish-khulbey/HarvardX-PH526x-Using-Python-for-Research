# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

# text = "This is just a test string. I repeat, this is a text string"


def count_words(text):
    """
    Skip punctutation
    Create a dictionary for word, count
    """
    text.lower()
    skips = [".", ",", ";", "'", '"', ":"]
    for ch in skips:
        text = text.replace(ch, "")

    # word_counts = {}
    # for word in text.split(" "):
    #     if word in word_counts:
    #         word_counts[word] += 1
    #     else:
    #         word_counts[word] = 1
    word_counts = Counter(text.split(" "))
    return word_counts


def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
        return text


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


def multiple_reads():
    stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
    title_num = 1
    book_dir = "./Books"
    for language in os.listdir(book_dir):
        for author in os.listdir(book_dir + "/" + language):
            for title in os.listdir(book_dir + "/" + language + "/" + author):
                inputfile = book_dir + "/" + language + "/" + author + "/" + title
                # print(inputfile)
                text = read_book(inputfile)
                (num_unique, counts) = word_stats(count_words(text))
                stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
                title_num += 1
    return stats


# title_path = "./English/shakespeare/Romeo and Juliet.txt"
stats = multiple_reads()
print(stats.head())
print(stats.tail())
plt.plot(stats.length, stats.unique, 'bo')
plt.loglog(stats.length, stats.unique, 'bo')
plt.figure(figsize=(10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")

# text = read_book(title_path)
# print(len(text))
# ind = text.find("What's in a name?")
# print(ind)
# word_counts = count_words(text)
# print(word_counts)
# (num_unique, counts) = word_stats(word_counts)
# print(num_unique, sum(counts))
