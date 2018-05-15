import sys
file = sys.argv[1]


f = open(file, 'r')

lines = f.readlines()

arr = []
result_arr = []
out_arr = []

for x in range(0, 999):
	arr.append(0)

for line in lines:
	if len(line.split(' ')) == 2:
		line_arr = line.split(' ')
		command = line_arr[0]
		number = int(line_arr[1])

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
	else:
		out_arr.append(int(line))

flag = True
if len(result_arr) != len(out_arr):
	flag = False
	print(flag)
else:
	for x in range(0, len(result_arr)):
		if result_arr[x] != int(out_arr[x]):
			flag = False
	print(flag)