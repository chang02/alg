import sys
import random

def partition(input, p, r, i):
	input[0], input[i] = input[i], input[0]

	j = p+1
	for x in range(p+1, r+1):
		if input[p] < input[x]:
			pass
		else:
			input[j], input[x] = input[x], input[j]
			j = j + 1

	input[j-1], input[p] = input[p], input[j-1]

	return j-1

def insertionSort(input):
    for x in range(1, len(input)):
        val = input[x]
        i = x
        while i > 0 and input[i-1] > val:
            input[i] = input[i-1]
            i -= 1
        input[i] = val

def median_of_five(five):
	insertionSort(five)
	return five[len(five)//2]

def find_median(input):
	i = 0
	divided_input = []
	temp_input = []
	#combine with 5 elements
	for x in range(0,len(input)):
		if x % 5 == 0 and x != 0:
			divided_input.append(temp_input)
			temp_input = []
		temp_input.append(input[x])
		if x == len(input) - 1:
			divided_input.append(temp_input)
	
	if len(divided_input) == 1:
		return median_of_five(divided_input[0])

	#new list of medians
	medians = []
	for division in divided_input:
		medians.append(median_of_five(division))

	return find_median(medians)

def rselect(input, i):
	ran = random.randrange(0, len(input))

	q = partition(input, 0, len(input)-1, ran)
	if q == i-1:
		return input[q]
	elif q > i-1:
		new_input = list(input[0:q])
		return rselect(new_input, i)
	else:
		new_input = list(input[q+1:])
		return rselect(new_input, i-q-1)

def dselect(input, i):
	median = find_median(input)
	index = input.index(median)

	q = partition(input, 0, len(input)-1, index)
	if q == i-1:
		return input[q]
	elif q > i-1:
		new_input = list(input[0:q])
		return dselect(new_input, i)
	else:
		new_input = list(input[q+1:])
		return dselect(new_input, i-q-1)

#get input start
index = int(sys.argv[1])
filename = sys.argv[2]

f = open(filename, 'r')
lines = f.readlines()

input = []

for line in lines:
	line_arr = line.split(" ")
	for number in line_arr:
		input.append(int(number))
#get input complete


test = []
for x in range(0, 2000):
   test.append(random.randint(1,2000))

flag = False
for i in range(200):
    a = random.randint(1, 2000)
    flag =  rselect(test, 1) == dselect(test, 1) == sorted(test)[0] and rselect(test, 100) == dselect(test, 100) == sorted(test)[99] and rselect(test, a) == dselect(test, a) == sorted(test)[a-1] and rselect(test, 200) == dselect(test, 200) == sorted(test)[199]

    if(flag == False):
        print("이창영 바보 멍청이")