#!/usr/bin/env python3
# check if sentence is a pangram
from string import ascii_lowercase


def is_pangram(sentence):
# sentence: sentence to check

    if not sentence:
        return False

    # store lowercase alphabet
    alphabetList = list(ascii_lowercase)
    # make sentence all lowercase
    sentenceList = list(sentence.lower())
    """
    create new list with only letters in the Lcase alphabet
    this way don't have to worry about spaces or underscores
    although creating new list is less space efficient
    """
    resultsList = [letter for letter in sentenceList if letter in alphabetList]

    return len(alphabetList) == len(list(set(resultsList)))
