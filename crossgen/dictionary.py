from string import ascii_lowercase as alphabet_st
import os
import json
import sys


def create_files(files):
    if not files:
        return False

    if not os.path.exists("dictonaries/" + files[0] + "_set"):
        os.mkdir("dictonaries/" + files[0] + "_set")
    else:
        sys.exit("set with this name already exists")

    words = open(files[1], "r")
    words_lines = words.readlines()
    words.close()

    cor_words = []
    cor_meanings = []
    for word in words_lines:
        split = word.find("|")
        meaning = word[split + 1 :]
        word = word[:split]
        word = word.strip("\n").strip(" ").lower()
        if word.isalpha():
            cor_words.append(word)
            cor_meanings.append(meaning.strip("\n"))
    set_words = json.dumps(cor_words)
    set_meanings = json.dumps(cor_meanings)

    words_new = open("dictonaries/" + files[0] + "_set/word.txt", "w+")
    meanings_new = open("dictonaries/" + files[0] + "_set/meaning.txt", "w+")
    words_new.write(set_words)
    meanings_new.write(set_meanings)
    words_new.close()
    meanings_new.close()
    return cor_words


def match_pos(cor_words, files):
    alphabet = {}
    for let in alphabet_st:
        alphabet[let] = [[] for j in range(25)]

    file = open("dictonaries/" + files[0] + "_set/position.txt", "w+")
    for key, val in enumerate(cor_words):
        sub_key = 0

        for letter in val:
            alphabet[letter][sub_key].append(key)
            sub_key += 1

    file.write(json.dumps(alphabet))
    file.close()


def create_set(files):
    words = create_files(files)
    if words:
        match_pos(words, files)
