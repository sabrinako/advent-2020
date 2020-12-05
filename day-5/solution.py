"""
--- Day 5: Binary Boarding ---

First puzzle answer: 828
Second puzzle answer: 
"""
def puzzle2():
	"""
	puzzle 2
	"""
	with open("input.txt") as file:
		seat_strings = file.read().split("\n")
		list_ids = []

		for seat_str in seat_strings:
			row, seat = find_seat_id(seat_str)
			
			if 0 < row < 127:
				list_ids.append(row * 8 + seat)

		list_ids.sort()

		counter = 1
		for num in range(list_ids[1], list_ids[-2]):
			if num != list_ids[counter]:
				return num
			counter += 1


def find_seat_id(seat_string):
	"""
	puzzle 1
	function for figuring out the seat location based on binary seat identifier

	keyword
	---
	seat: the string representation of seat location, consisting of F's, B's, L's, and R's' 
		  the 1st 7 characters are the representation of the row 
		  
	return value
	---
	row, seat
	"""
	steps = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]

	row_range = [1, 128]
	seat_range = [1, 8]
	i = 0
	#calculate the row
	for letter in seat_string:
		if letter == "F":
			row_range[1] -= steps[i]
		elif letter == "B":
			row_range[0] += steps[i]
		elif letter == "L":
			seat_range[1] -= steps[i]
		elif letter == "R":
			seat_range[0] += steps[i]
		i += 1
	return row_range[0] - 1, seat_range[0] - 1


def puzzle1():
	with open("input.txt") as file:
		seat_strings = file.read().split("\n")
		highest_seat_id = 0

		for seat in seat_strings:
			row, seat = find_seat_id(seat)
			seat_num = row * 8 + seat

			if seat_num > highest_seat_id:
				highest_seat_id = seat_num

		return highest_seat_id

if __name__ == "__main__":
	high_seat = puzzle1()
	print(high_seat)
	my_seat = puzzle2()
	print(my_seat)
