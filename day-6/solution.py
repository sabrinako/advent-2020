"""
--- Day 6: Custom Customs ---
First puzzle answer: 6335
Second puzzle answer: 3392
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def puzzle2():
	with open("input.txt") as file:
		file_split = file.read().split("\n\n")
		answers_list = [line.split("\n") for line in file_split]

		total_count = 0

		for answers in answers_list:
			viewed_answers = {letter:0 for letter in alphabet}
			print(answers)
			total_people = 0
			for line in answers:
				total_people += 1
				for letter_view in line:
					viewed_answers[letter_view] += 1
			
			for letter_check in viewed_answers:
				if viewed_answers[letter_check] == total_people:
					print("%s: %s"%(letter_check, viewed_answers[letter_check]))
					total_count += 1

		return total_count


def puzzle1():
	with open("input.txt") as file:
		file_split = file.read().split("\n\n")
		answers_list = [line.replace("\n", "") for line in file_split]

		total_count = 0

		for answers in answers_list:
			viewed_answers = {letter:False for letter in alphabet}
			counter = 0
			for current_letter in answers:
				if not viewed_answers[current_letter]:
					viewed_answers[current_letter] = True
					counter += 1
			total_count += counter

		return total_count


if __name__ == "__main__":
	final_count = puzzle1()
	print(final_count)
	second_count = puzzle2()
	print(second_count)
