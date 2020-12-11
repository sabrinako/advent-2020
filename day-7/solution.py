"""
--- Day 7: Handy Haversacks ---
First puzzle answer: 131
Second puzzle answer: 11261
"""
import re

rules_dict = {}
total_count = 0

def recursive_bag_search(bag_color):
	for color in rules_dict[bag_color]:
		if color == "no other":
			return False
		elif color == "shiny gold":
			return True
		if recursive_bag_search(color):
			return True


def puzzle1():
	with open("input.txt") as file:
		rule_split = file.read().splitlines()

		for rule in rule_split:
			# split the outermost bag from the possible inner bags
			outer_inner = rule.split(" bags contain ")
			#clean up the inner bag rules string to just have the colors + split colors
			outer_inner[1] = re.sub(r'([0-9] )', '', outer_inner[1])
			outer_inner[1] = re.sub(r'(bags|bag)', '', outer_inner[1])
			outer_inner[1] = outer_inner[1].replace(" .", "")
			inner_list = outer_inner[1].split(" , ")
			#add to dictionary
			rules_dict[outer_inner[0]] = inner_list

		bag_count = 0
		for top_color in rules_dict:
			can_hold = recursive_bag_search(top_color)

			if can_hold == True:
				bag_count += 1

		return bag_count


def gold_count(color, last_count):
	global total_count
	"""
	shiny gold: 4 muted violet, 3 dark lime
	muted violet: 4 pale green
	pale green: end (20)
	"""
	current_dict = rules_dict[color]
	for rule in current_dict:
		if rule == "other":
			break
		else:
			new_count = last_count * current_dict[rule]
			total_count += new_count
			gold_count(rule, new_count)



def puzzle2():
	global total_count
	with open("input.txt") as file:
		rule_split = file.read().splitlines()

		for rule in rule_split:
			outer_inner = rule.split(" bags contain ")
			outer_inner[1] = re.sub(r'(bags|bag)', '', outer_inner[1])
			outer_inner[1] = outer_inner[1].replace(" .", "")
			inner_list = outer_inner[1].split(" , ")
			inner_dict = {}
			for inner_rule in inner_list:
				in_split = inner_rule.split(" ", 1)
				if in_split[0] == "no":
					inner_dict[in_split[1]] = 0
				else:
					inner_dict[in_split[1]] = int(in_split[0])

			rules_dict[outer_inner[0]] = inner_dict

	for color in rules_dict["shiny gold"]:
		this_count = rules_dict["shiny gold"][color]
		total_count += this_count
		gold_count(color, this_count)

	return total_count



if __name__ == "__main__":
	bag_color_count = puzzle1()
	print(bag_color_count)
	gold_count = puzzle2()
	print(gold_count)
