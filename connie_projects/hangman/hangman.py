"""
File: hangman.py
Name: Connie Huang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1. Print starting words and set up random answer
    2. Ask for an input.
      If not alpha, return wrong message and do not calculate.
      If it's alpha, change all of them to upper case to be case-insensitive
    3. If input is correct, substitute the character in the same location as the answer.
        For the rest, keep it the same as before and save the result as dashed.
        When dashed == answer, win the game.
    4. If input is wrong, count +1.
        When count == N_TURNS, show that game-over
    """
    answer = random_word()
    print('THe word looks like ' + length_of_answer(answer))
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    input_ch = input('Your guess: ').upper()
    # Show number of characters using '-'
    dashed = length_of_answer(answer)
    count = 0
    while True:
        # To avoid input not alpha.
        if input_ch.isalpha() is False:
            print('Illegal format.')
            input_ch = input('Your guess: ').upper()
        elif len(input_ch) != 1:
            print('Illegal format.')
            input_ch = input('Your guess: ').upper()
        else:
            if input_ch in answer:
                for i in range(len(answer)):
                    # Substitute correct input. If not match, keep what it is when entering the loop.
                    if input_ch == answer[i]:
                        dashed = dashed[:i] + input_ch + dashed[(i+1):(len(answer)+1)]
                print('You are correct!')
                if dashed == answer:
                    print('You win!!')
                    print('The word was: ' + answer)
                    break
            else:
                count += 1
                print('There is no ' + input_ch + "'s in the word.")

                if count == N_TURNS:
                    print('You are completely hung :(')
                    print('The word is ' + answer)
                    hangman_picture(N_TURNS, count)
                    break
            print('The word looks like ' + dashed)
            print('You have ' + str(N_TURNS - count) + ' wrong guesses left.')
            hangman_picture(N_TURNS, count)
            input_ch = input('You guess: ').upper()


def hangman_picture(n, c):
    """
    Will only show up the figure when it's the multiple of 6.
    Always show the last one when it's game-over.
    n = total number of guesses (N_TURNS)
    c = count
    return: hangman graph
    """
    s = n//6
    head = '|  O   '
    body = '|  |'
    left_hand = '| /|'
    right_hand = '| /|\\'
    left_leg = '| /'
    right_leg = '| / \\'
    last = '|you=dead!'
    top = '-------'
    wall = '|'
    if c < s:
        print(top)
        print(wall)
        print(wall)
        print(wall)
        print(wall)
    if s <= c < s*2:
        print(top)
        print(head)
        print(wall)
        print(wall)
        print(wall)
    if s*2 <= c < s*3:
        print(top)
        print(head)
        print(body)
        print(wall)
        print(wall)
    if s*3 <= c < s*4:
        print(top)
        print(head)
        print(left_hand)
        print(wall)
        print(wall)
    if s*4 <= c < s*5:
        print(top)
        print(head)
        print(right_hand)
        print(wall)
        print(wall)
    if s*5 <= c < s*6:
        print(top)
        print(head)
        print(right_hand)
        print(left_leg)
        print(wall)
    if s*6 <= c < n:
        print(top)
        print(head)
        print(right_hand)
        print(right_leg)
        print(wall)
    if c == n:
        print(top)
        print(head)
        print(right_hand)
        print(right_leg)
        print(last)


def length_of_answer(n):
    """
    To get the '-' based on how many characters there are in the input
    n = input
    """
    length = len(n)
    dashed_result = ''
    for i in range(length):
        # print('-', end='') -> don't need to print since I've added them together in next line.
        dashed_result += '-'
    return dashed_result


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
