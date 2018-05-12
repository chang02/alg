import sys
in_file = sys.argv[1]
out_file = sys.argv[2]

in_f = open(in_file, 'r')
out_f = open(out_file, 'r')

in_lines = in_f.readlines()
out_lines = out_f.readlines()

arr = []
result_arr = []
for x in range(0, 1000):
	arr.append(0)

for in_line in in_lines:
	in_line_arr = in_line.split(' ')
	command = in_line_arr[0]
	number = int(in_line_arr[1])

	if command == 'I':
		if arr[number-1] == 1:
			result_arr.append(0)
		elif arr[number-1] == 0:
			arr[number-1] = 1
			result_arr.append(number)
	elif command == 'D':
		if arr[number-1] == 1:
			arr[number-1] = 0
			result_arr.append(number)
		elif arr[number-1] == 0:
			result_arr.append(0)
	elif command == 'S':
		count = 0
		for x in range(0, len(arr)):
			if arr[x] == 1:
				count = count + 1
			if count == number:
				result_arr.append(x+1)
				break
		if count < number:
			result_arr.append(0)
	elif command == 'R':
		count = 0
		if arr[number-1] == 0:
			result_arr.append(0)
		else:
			for x in range(0, number):
				if arr[x] == 1:
					count = count + 1
			result_arr.append(count)

flag = True
if len(result_arr) != len(out_lines):
	flag = False
	print(flag)
else:
	for x in range(0, len(result_arr)):
		if result_arr[x] != int(out_lines[x]):
			flag = False
	print(flag)