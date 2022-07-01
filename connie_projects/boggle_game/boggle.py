"""
File: boggle.py
Name: Connie Huang
----------------------------------------
TODO:
1. Ask for inputs.
2. See whether there are different word combination using the inputs.
3. Print out the result and add up the total.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dictionary = []


def main():
	"""
	TODO:
	1. Ask for input and check whether it fits required format.
	2. Put input into a dictionary with it's (row, column) as key and character as val.
	3. Add up number of results and print.
	"""
	start = time.time()
	matrix = []
	d = {}
	read_dictionary()
	start_no = 0
	# to add input to a list
	for i in range(4):
		row_i = str(input(str(i+1)+' row of letters: '))
		if format_check(row_i.lower()) is False:
			print('Illegal input')
			break
		else:
			for ch in row_i:
				if ch.isalpha() is True:
					matrix.append(ch.lower())
	for i in range(4):
		for j in range(4):
			d[(i, j)] = matrix[start_no]
			start_no += 1
	result_lst = []
	word = ''
	find_result(d, word, result_lst)
	print('There are', len(result_lst), 'words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')

# def helper(lst, no_of_result, word, row_column_matrix, result_lst):


def find_result(ch_position, word, result_lst):
	"""
	:param ch_position: dictionary with position as key and input character as val.
	:param word: character that will be added.
	:param result_lst: after printing the result, it will be added to the list.
	:return: list. (result_lst)
	-------------------------------------------
	Add first character before going to helper to make sure all possibility is checked.
	"""
	for i in range(4):
		for j in range(4):
			word += ch_position[(i, j)]
			helper(ch_position, word, result_lst, [(i, j)])
			word = ""


def helper(ch_position, word, result_lst, used_position):
	"""
	:param ch_position: dictionary with position as key and input character as val.
	:param word: character that will be added.
	:param result_lst: after printing the result, it will be added to the list.
	:param used_position: if word added, it's position will be added to this list to avoid using twice.
	:return: list. (result_lst)
	-------------------------------------------
	Add neighbor characters to the word and see whether it's in dictionary. If yes, add to result_lst.
	"""
	# to get the position of first character
	row = used_position[-1][0]
	col = used_position[-1][1]
	if word in dictionary and len(word) >= 4 and word not in result_lst:
		print(f'Found "{word}"')
		result_lst.append(word)
		helper(ch_position, word, result_lst, used_position)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				n_row = row + i
				n_col = col + j
				if n_row < 0 or n_col < 0 or n_row >= 4 or n_col >= 4:
					pass
				elif (n_row, n_col) in used_position:
					pass
				else:
					word += ch_position[n_row, n_col]
					used_position.append((n_row, n_col))
					if has_prefix(word) is False:
						pass
					else:
						helper(ch_position, word, result_lst, used_position)
					word = word[:-1]
					used_position.pop(-1)


def format_check(row_input):
	# To check whether format is same as requested.
	if len(row_input) != 7:
		return False
	elif row_input[1] is not " " or row_input[3] is not " " or row_input[5] is not " ":
		return False
	elif row_input[0].isalpha() is False or row_input[2].isalpha() is False or row_input[4].isalpha() is False or row_input[6].isalpha() is False:
		return False
	else:
		return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for words in f:
			# word = words.split()
			dictionary.append(words.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
