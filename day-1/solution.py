"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

First puzzle answer: 381699
Second puzzle answer: 111605670
"""
def first_solution_pt1():
	file = open("input.txt", "r")
	num_array = []

	for num in file:
		num_array.append(int(num))

	for x in range(len(num_array)):
		for y in range(len(num_array) - 1):
			if num_array[x] + num_array[y] == 2020:
				product = num_array[x] * num_array[y]
				print(product)
				return product


def first_solution_pt2():
	file = open("input.txt", "r")
	num_array = []

	for num in file:
		num_array.append(int(num))

	for x in range(len(num_array)):
		for y in range(len(num_array) - 1):
			for z in range(len(num_array) - 2):
				if num_array[x] + num_array[y] + num_array[z] == 2020:
					product = num_array[x] * num_array[y] * num_array[z]
					print(product)
					return product


def second_solution_pt1():
	'''
	keep an array of the result of subtracting a viewed number from 2020,
	and if we find this resulting number later and compare to the array
	we'll find out we have a match
	'''
	file = open("input.txt", "r")
	remainder_array = []

	for x in file:
		num = int(x)
		if num not in remainder_array:
			remainder_array.append(2020 - num)
		else:
			product = (2020 - num) * num
			print(product)



if __name__ == "__main__":
	second_solution_pt1()
	first_solution_pt2()
