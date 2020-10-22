#!/usr/bin/env python


def compare_func():

	list_numbers = []
	dict_seen = {} 
	result = {}
	with open("file_numbers") as file:
		numbers = [number.strip() for number in file]
		for number in numbers:
			if number not in dict_seen:
			   dict_seen[number] = 1
			else:
			   dict_seen[number] += 1
			for key,value in dict_seen.items():
			    if int(value) > 1:
			        result[key] = dict_seen[key]
		return (result)

print(compare_func())
