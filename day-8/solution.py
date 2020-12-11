"""
--- Day 8: Handheld Halting ---
First puzzle answer: 
Second puzzle answer: 
"""
import copy


instruction_list = []
viewed_indexes = []

def traverse_code(index, list, current_total):
	global viewed_indexes
	if index in viewed_indexes:
		viewed_indexes = []
		return False, current_total

	if index == len(list):
		viewed_indexes = []
		return True, current_total

	instruction, num = list[index].split(" ")

	if instruction == "nop":
		viewed_indexes.append(index)
		return traverse_code(index + 1, list, current_total)
	elif instruction == "acc":
		viewed_indexes.append(index)
		total = current_total + int(num)
		return traverse_code(index + 1, list, total)
	elif instruction == "jmp":
		viewed_indexes.append(index)
		return traverse_code(index + int(num), list, current_total)

def change_nop_jmp(change_index):
	modified_instructions = copy.deepcopy(instruction_list)
	if "nop" in instruction_list[change_index]:
		modified_instructions[change_index] = "jmp " + modified_instructions[change_index].split(" ")[1]
	else:
		modified_instructions[change_index] = "nop " + modified_instructions[change_index].split(" ")[1]
	end_hit_bool, change_total = traverse_code(0, modified_instructions, 0)
	return end_hit_bool, change_total

def puzzle1():
	global instruction_list
	with open("input.txt") as file:
		instruction_list = file.read().splitlines()

	hit_end, final_count = traverse_code(0, instruction_list, 0)
	return final_count


def puzzle2():
	global last_index_hit
	for i in range(len(instruction_list)):
		line = instruction_list[i]
		if "nop" in line or "jmp" in line:
			hit_bool, count = change_nop_jmp(i)
			if hit_bool:
				return count


if __name__ == "__main__":
	total_before_loop = puzzle1()
	print(total_before_loop)
	final_total = puzzle2()
	print(final_total)
