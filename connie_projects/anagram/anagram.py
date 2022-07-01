"""
File: anagram.py
Name: Connie Huang
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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dictionary = []


def main():
    """
    TODO:
    1. Ask for an input of a word.
    2. Create a find_anagrams_helper to find all possibilities.
    3. Print number of opportunities and all the result.
    """
    print('Welcome to stanCode "Anagram Generator" (or', EXIT, 'to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        read_dictionary()
        if word == EXIT:
            break
        else:
            find_anagrams(word)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for words in f:
            word = words.strip()
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s: Input
    :return: print of count and list
    """
    print('Searching...')
    result_lst = find_anagrams_helper(s, [], len(s), '', [])
    print(len(result_lst), ' anagrams: ', result_lst)


def find_anagrams_helper(s, current_lst, length, result, final_lst):
    """
    :param s: input of the word
    :param current_lst: Permutation of the characters
    :param length: how many digit s has
    :param result: one of the permutation results
    :param final_lst: list, result of list
    :return: list containing all the results
    """
    if len(current_lst) == len(s):
        for i in range(len(current_lst)):
            result += current_lst[i]
        if result not in final_lst and result in dictionary:
            print('Found: ' + result)
            final_lst.append(result)
            print('Searching...')
    else:
        for i in range(len(current_lst)):
            result += current_lst[i]
        if has_prefix(result) is False:
            result = ''
            pass
        else:
            for ch in s:
                num_ch = s.count(ch)
                # the situation of all character only showing up once.
                if num_ch == 1:
                    if ch in current_lst:
                        pass
                    else:
                        # choose
                        current_lst.append(ch)
                        result = ''
                        # explore
                        find_anagrams_helper(s, current_lst, length, result, final_lst)
                        # un-choose
                        current_lst.pop()
                else:
                    if ch in current_lst and current_lst.count(ch) == num_ch:
                        pass
                    else:
                        # choose
                        current_lst.append(ch)
                        result = ''
                        # explore
                        find_anagrams_helper(s, current_lst, length, result, final_lst)
                        # un-choose
                        current_lst.pop()
    return final_lst


def has_prefix(sub_s):
    """
    :param sub_s: current words in result.
    :return: True/False. Whether there's any dictionary starting with sub_s.
    """
    for word in dictionary:
        if word.startswith(sub_s) is True:
            return True
    return False
    # 'coding'.startswith('co') -> True
    # 'standard'.startswith('stat') -> False. If false, we should stop searching.


if __name__ == '__main__':
    main()
