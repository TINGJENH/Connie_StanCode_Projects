"""
File: coin_flip_runs.py
Name: Connie Huang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	1. Print 'Let's flip a coin!' and ask for an input for number of runs.
	2. Get first random character, either H or T, and add it to the result.
	3. Assume there's no run and not having same character in the beginning.
	4. Will continuously ask for a new character and add to result until there's same character showing up
	   twice consecutively and count of the run equals to the number of runs input.
	5. Print the result.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	random_1 = chr(r.randrange(ord('H'), ord('U'), 12))
	result = random_1
	is_a_run = False
	total_run = 0
	while True:
		random_2 = chr(r.randrange(ord('H'), ord('U'), 12))
		if random_1 == random_2:
			if not is_a_run:
				total_run += 1
				is_a_run = True
		else:
			random_1 = random_2
			is_a_run = False
		result += random_2
		if total_run == num_run:
			break
	print(result)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
