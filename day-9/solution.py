"""
--- Day 9: Encoding Error ---
First puzzle answer: 
Second puzzle answer: 
"""
lines = []

def traverse_sum(break_num, index=0, set=None):
	if set is None:
		set = []
	
	if index < len(lines):
		set.append(int(lines[index]))

		if sum(set) == break_num:
			return set
		elif sum(set) > break_num:
			return None
		else:
			return traverse_sum(break_num, index + 1, set)
	else:
		return None



def puzzle2(break_num):
	global lines
	
	for i in range(len(lines)):
		current_set = traverse_sum(break_num, i)

		if current_set is not None:
			print(sum(current_set))
			current_set.sort()
			return current_set[0] + current_set[-1]
			

def puzzle1():
	global lines
	current_selection = []

	for i in range(len(lines)):
		current_num = int(lines[i])
		breakpoint_found = True

		if i > 25:
			breakpoint_found = False
			current_selection.pop(0)
			possible_addends = []
			for x in current_selection:
				if x not in possible_addends:
					possible_addends.append(current_num - x)
				else:
					breakpoint_found = True
					break

		if not breakpoint_found:
			return current_num

		current_selection.append(current_num)


if __name__ == "__main__":
	with open("input.txt") as file:
		lines = file.read().splitlines()

	break_num = puzzle1()
	print(break_num)
	top_btm_sum = puzzle2(break_num)
	print(top_btm_sum)
