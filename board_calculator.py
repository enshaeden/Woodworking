# v1.0 completed Dec 4, 2022
# Author - enshaeden


import os
import pprint


def clear():
	os.system('clear')


def starting_measurements():
	# Choose metric or imperial measurements
	metric_or_imperial = input(f"Are you using imperial or metric? [i/m]\n")
	# set the length of each board for calculation
	board_length = input(f"What is the board length for calculation? (ft or m)\n")
	board_length = float(board_length)
	if metric_or_imperial == "i":
		board_length = float(board_length * 12)
	elif metric_or_imperial == "m":
		board_length = float(board_length * 100)
	clear()
	return board_length


def dimension_selection():
		board_type = input(f"""
Which board dimension are you using?
1x
1) 2
2) 3
3) 4

2x
4) 4
5) 6
6) 8
7) 10
8) 12

4x
9) 4

=> """)
		clear()
		return board_type


def stock_length_calculator(project_boards_cuts, board_type, board_length):
	minimum_boards = 1
	remnants = []
	# prompt for length of cut
	length_of_cut = input(f"How long is each cut?\n")
	length_of_cut = float(length_of_cut)
	# prompt for number of cuts needed
	number_of_cuts = input(f"How many do you need?\n")
	number_of_cuts = int(number_of_cuts)
	# sets the minimum board length to the calculated board length in __main__
	board_length = board_length
	# creates a calculable variable for each board
	cut_board = board_length
	for i in range(1, number_of_cuts):
		# make sure there are no remnants from previous cuts that can be used instead
		spare_checker = remnant_check(project_boards_cuts, board_type, length_of_cut)
		if spare_checker == "y":
			print("removing remnant")     # remove after testing
			remove_from_list(project_boards_cuts, board_type, length_of_cut)
		else:
			# subtract the length of the cut from the calcuable board
			cut_board -= length_of_cut
			# if the next cut is larger than the remnant of calcuable board
			if length_of_cut > cut_board:
				minimum_boards += 1
				# add the remainder of the caluable board to list of remnants
				remnants.append(cut_board)
				# set the calcuable board back to the minimum board length
				cut_board = board_length
	return minimum_boards, remnants, project_boards_cuts
		

def add_to_list(project_boards_cuts, board_type, number_of_boards, extra_cuts):
	if board_type == "1":
		project_boards_cuts['boards_needed']['onebytwo'].append(number_of_boards)
		project_boards_cuts['remnants']['onebytwo'].append(extra_cuts)
	elif board_type == "2":
		project_boards_cuts['boards_needed']['onebythree'].append(number_of_boards)
		project_boards_cuts['remnants']['onebythree'].append(extra_cuts)
	elif board_type == "3":
		project_boards_cuts['boards_needed']['onebyfour'].append(number_of_boards)
		project_boards_cuts['remnants']['onebyfour'].append(extra_cuts)
	elif board_type == "4":
		project_boards_cuts['boards_needed']['twobyfour'].append(number_of_boards)
		project_boards_cuts['remnants']['twobyfour'].append(extra_cuts)
	elif board_type == "5":
		project_boards_cuts['boards_needed']['twobysix'].append(number_of_boards)
		project_boards_cuts['remnants']['twobysix'].append(extra_cuts)
	elif board_type == "6":
		project_boards_cuts['boards_needed']['twobyeight'].append(number_of_boards)
		project_boards_cuts['remnants']['twobyeight'].append(extra_cuts)
	elif board_type == "7":
		project_boards_cuts['boards_needed']['twobyten'].append(number_of_boards)
		project_boards_cuts['remnants']['twobyten'].append(extra_cuts)
	elif board_type == "8":
		project_boards_cuts['boards_needed']['twobytwelve'].append(number_of_boards)
		project_boards_cuts['remnants']['twobytwelve'].append(extra_cuts)
	elif board_type == "9":
		project_boards_cuts['boards_needed']['fourbyfour'].append(number_of_boards)
		project_boards_cuts['remnants']['fourbyfour'].append(extra_cuts)
	return project_boards_cuts


def remove_from_list(project_boards_cuts, board_type, length_of_cut):
	if board_type == "1":
		project_boards_cuts['remnants']['onebytwo'].remove(length_of_cut)
	elif board_type == "2":
		project_boards_cuts['remnants']['onebythree'].remove(length_of_cut)
	elif board_type == "3":
		project_boards_cuts['remnants']['onebyfour'].remove(length_of_cut)
	elif board_type == "4":
		project_boards_cuts['remnants']['twobyfour'].remove(length_of_cut)
	elif board_type == "5":
		project_boards_cuts['remnants']['twobysix'].remove(length_of_cut)
	elif board_type == "6":
		project_boards_cuts['remnants']['twobyeight'].remove(length_of_cut)
	elif board_type == "7":
		project_boards_cuts['remnants']['twobyten'].remove(length_of_cut)
	elif board_type == "8":
		project_boards_cuts['remnants']['twobytwelve'].remove(length_of_cut)
	elif board_type == "9":
		project_boards_cuts['remnants']['fourbyfour'].remove(length_of_cut)
	return project_boards_cuts


def remnant_check(project_boards_cuts, board_type, length_of_cut):
	# set board type from numerical value to dict key value
	if board_type == "1":
		board_type = "onebytwo"
	elif board_type == "2":
		board_type = "onebythre"
	elif board_type == "3":
		board_type = "onebyfour"
	elif board_type == "4":
		board_type = "twobyfour"
	elif board_type == "5":
		board_type = "twobysix"
	elif board_type == "6":
		board_type = "twobyeight"
	elif board_type == "7":
		board_type = "twobyten"
	elif board_type == "8":
		board_type = "twobytwelve"
	elif board_type == "9":
		board_type = "fourbyfour"
	# check if a remnant exists
	if length_of_cut in project_boards_cuts['remnants'][board_type]:
		print("remnant found")     # remove after testing
		remnant_check = "y"
	else:
		remnant_check = "n"
	return remnant_check

		
def main():
	project_boards_cuts = {
		'boards_needed': {
			'onebytwo': [],
			'onebythree': [],
			'onebyfour': [],
			'twobyfour': [],
			'twobysix': [],
			'twobyeight': [],
			'twobyten': [],
			'twobytwelve': [],
			'fourbyfour': []
		},
		'remnants': {
			'onebytwo': [],
			'onebythree': [],
			'onebyfour': [],
			'twobyfour': [],
			'twobysix': [],
			'twobyeight': [],
			'twobyten': [],
			'twobytwelve': [],
			'fourbyfour': []
		}
	}
	clear()
	board_length = starting_measurements()
	proceed = True
	while proceed:
		# select dimensional lumber for calculation
		board_type = dimension_selection()
		# calculate number of boards required
		number_of_boards, extra_cuts, project_boards_cuts = stock_length_calculator(project_boards_cuts, board_type, board_length)
		# add boards to list
		project_boards_cuts = add_to_list(project_boards_cuts, board_type, number_of_boards, extra_cuts)
		want_to_proceed = input(f"Do you have any more boards to calculate? [y/n]\n")
		if want_to_proceed == "n":
			proceed = False
	# print final project needs
	pprint.pp(project_boards_cuts)
	

if __name__ == "__main__":
	main()
	
	
# TODO figure out why remnant_check always leaves one spare
# TODO create GUI interface
# TODO create .run