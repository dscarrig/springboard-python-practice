"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(this, file):
        with open(file) as f:
            this.words = f.readlines()


    def random(this):
        rand_num = random.randrange(0, len(this.words))
        return this.words[rand_num]


    def all_lines_len(this):
        return len(this.words)

word_finder = WordFinder("words.txt")
print(word_finder.random())
