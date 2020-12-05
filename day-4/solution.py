"""
--- Day 4: Passport Processing ---

First puzzle answer: 204
Second puzzle answer: 179
"""
import re


def validate_regex_fields(regex, value):
	return re.search(regex, value)


def validate_in_range(range, value):
	"""
	range is a tuple
	"""
	return range[0] <= int(value) <= range[1]


def validate_year_field(name, value):
	year_ranges = {
		"byr": (1920, 2002),
		"iyr": (2010, 2020),
		"eyr": (2020, 2030)
	}

	regex_pass = validate_regex_fields("[0-9]{4}", value)
	range_pass = validate_in_range(year_ranges[name], value)
	return (regex_pass and range_pass)


def validate_passport_fields(field_name, field_value):
	"""
	byr (Birth Year) - four digits; at least 1920 and at most 2002.
	iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	hgt (Height) - a number followed by either cm or in:
	If cm, the number must be at least 150 and at most 193.
	If in, the number must be at least 59 and at most 76.
	hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	pid (Passport ID) - a nine-digit number, including leading zeroes.
	cid (Country ID) - ignored, missing or not.
	"""

	if field_name == 'byr' and validate_year_field("byr", field_value):
		return True
	elif field_name == 'iyr' and validate_year_field("iyr", field_value):
		return True
	elif field_name == 'eyr'and validate_year_field("eyr", field_value):
		return True
	elif field_name == 'hgt' and validate_regex_fields("([0-9]{2,3}cm|in)", field_value):
		if "cm" in field_value:
			range_pass = validate_in_range((150,193), field_value[:-2])
		elif "in" in field_value:
			range_pass = validate_in_range((59,76), field_value[:-2])
		if range_pass:
			return True
	elif field_name == 'hcl' and validate_regex_fields("(#[a-f|0-9]{6})", field_value):
		return True
	elif field_name == 'ecl':
		acceptable_ecl = "amb blu brn gry grn hzl oth"
		if field_value in acceptable_ecl:
			return True
	elif field_name == 'pid' and validate_regex_fields("([0-9]{9})", field_value):
		return True
	return False


def validate_passport_full():
	"""
	Solution for part 2, similar to part 1 but also validates the
	actual values of the fields with helper functions
	"""
	acceptance_criteria = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

	with open("input.txt") as file:
		total_valid = 0

		file_split = file.read().split("\n\n")
		passport_list = [line.replace("\n", " ").split(" ") for line in file_split]

		for passport in passport_list:
			criteria_met = 0
			for field in passport:
				# gonna be honest and say i don't really know why but the last
				# passport returns an empty string within the list, which unless
				# caught with this, gets counted as valid, which apparently it shouldn't be
				if field == '':
					criteria_met = 0
				else:
					field_split = field.split(":")

				if field_split[0] in acceptance_criteria and validate_passport_fields(field_split[0], field_split[1]):
					criteria_met += 1
			if criteria_met == 7:
				print(passport)
				total_valid += 1

		return total_valid


def validate_passports():
	"""
	Solution for part 1
	"""
	# this is missing cid, which is the field that does not exist on north pole credentials and
	# stops them from being valid passports
	acceptance_criteria = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

	with open("input.txt") as file:
		total_valid = 0

		file_split = file.read().replace("\n", " ").split("  ")
		passport_list = [line.split(" ") for line in file_split]

		for passport in passport_list:
			criteria_met = 0
			for field in passport:
				if field.split(":")[0] in acceptance_criteria:
					criteria_met += 1
			if criteria_met == 7:
				total_valid += 1

		return total_valid



if __name__ == "__main__":
	result = validate_passports()
	print(result)
	result2 = validate_passport_full()
	print(result2)
