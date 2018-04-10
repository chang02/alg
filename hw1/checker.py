import sys

def check(arr, nth, value):
	lower = 0
	same = 0
	for x in arr:
		if x < value:
			lower = lower + 1
		if x == value:
			same = same + 1

	if lower < nth <= (lower + same):
		return True
	else:
		return False

nth = int(sys.argv[1])
filename = sys.argv[2]
value = int(sys.argv[3])

f = open(filename, 'r')
lines = f.readlines()

arr = []

for line in lines:
	line_arr = line.split(" ")
	for number in line_arr:
		if number != '' and number != '\n':
			arr.append(int(number))

result = check(arr, nth, value)
print(result)