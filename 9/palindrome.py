"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
from math import floor

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, "dictionary_m_words.txt")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt", DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word: str):
    """Return if word is palindrome, 'madam' would be one.
    Case insensitive, so Madam is valid too.
    It should work for phrases too so strip all but alphanumeric chars.
    So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word_list = [char.lower() for char in word if char.isalnum()]
    mid = floor(len(word_list) / 2)
    return word_list[:mid] == list(
        reversed(word_list[mid + 1 if len(word_list) % 2 else mid :])
    )


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
    If called without argument use the load_dictionary helper
    to populate the words list"""
    if words is None:
        words = load_dictionary()

    max_palindrome = None
    for word in words:
        if not is_palindrome(word=word):
            continue

        if not max_palindrome:
            max_palindrome = word
        else:
            max_palindrome = word if len(word) > len(max_palindrome) else max_palindrome

    return max_palindrome
