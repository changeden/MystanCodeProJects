"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
from campy.gui.events.timer import pause
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dictionary = [set() for i in range(26)]
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def main():
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit')
    word = str(input('Find anagrams for:'))

    if word == EXIT:
        pass
    else:
        read_dictionary()
        a = find_anagrams(word)
        count = 0
        for word in a:
            count += 1
            # print('Searching...')
            # print(f'Found: {word}')
        print(f'{count} anagrams: {a}')

def read_dictionary():

    with open(FILE, 'r') as f:
        for line in f:
            # word = line.strip()
            # dictionary.append(word)
            dictionary[ALPHABET.find(line[0])].add(line.lower().strip())

    # return dictionary


def find_anagrams(s):
    """
    :param s:
    :return:
    """

    letter_l = []

    for letter in s:
        letter_l.append(letter)

    return word_helper(s,letter_l, [], "", [])


def word_helper(s, s_list, word_lst, input_word, find_lst):


    #Base case:
    if len(s_list) == 0:
        if input_word not in find_lst:
            if input_word in dictionary[ALPHABET.find(input_word[0])]:
                find_lst.append(input_word)
                print('Searching...')
                print(f'Found: {input_word}')
    else:
        for word_letter in s:
            if word_letter not in input_word or word_letter in s_list:
                s_list.remove(word_letter)
                input_word += word_letter
                if has_prefix(input_word):
                    # Explore
                    word_helper(s, s_list, word_lst, input_word, find_lst)
                input_word = input_word[0:-1]
                s_list.append(word_letter)

    return find_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """

    for word in dictionary[ALPHABET.find(sub_s[0])]:
        if word.startswith(sub_s):
            return True
    return False

if __name__ == '__main__':
    main()

from campy.gui.events.timer import pause

