import sys
import random
import time

def partition(arr, p, r, i):
	arr[0], arr[i] = arr[i], arr[0]

	j = p+1
	for x in range(p+1, r+1):
		if arr[p] < arr[x]:
			pass
		else:
			arr[j], arr[x] = arr[x], arr[j]
			j = j + 1

	arr[j-1], arr[p] = arr[p], arr[j-1]

	return j-1

def insertionSort(a):
    for x in range(1, len(a)):
        val = a[x]
        i = x
        while i > 0 and a[i-1] > val:
            a[i] = a[i-1]
            i -= 1
        a[i] = val

def median_of_five(five):
	insertionSort(five)
	return five[len(five)//2]

def find_median(arr):
	i = 0
	divided_arr = []
	temp_arr = []
	#combine with 5 elements
	for x in range(0,len(arr)):
		if x % 5 == 0 and x != 0:
			divided_arr.append(temp_arr)
			temp_arr = []
		temp_arr.append(arr[x])
		if x == len(arr) - 1:
			divided_arr.append(temp_arr)
	
	if len(divided_arr) == 1:
		return median_of_five(divided_arr[0])

	#new list of medians
	medians = []
	for division in divided_arr:
		medians.append(median_of_five(division))

	return find_median(medians)

def rselect(arr, i):
	ran = random.randrange(0, len(arr))

	q = partition(arr, 0, len(arr)-1, ran)
	if q == i-1:
		return arr[q]
	elif q > i-1:
		new_input = list(arr[0:q])
		return rselect(new_input, i)
	else:
		new_input = list(arr[q+1:])
		return rselect(new_input, i-q-1)

def dselect(arr, i):
	median = find_median(arr)
	index = arr.index(median)

	q = partition(arr, 0, len(arr)-1, index)
	if q == i-1:
		return arr[q]
	elif q > i-1:
		new_input = list(arr[0:q])
		return dselect(new_input, i)
	else:
		new_input = list(arr[q+1:])
		return dselect(new_input, i-q-1)

#get input start
nth = int(sys.argv[1])
filename = sys.argv[2]

f = open(filename, 'r')
lines = f.readlines()

arr = []

for line in lines:
	line_arr = line.split(" ")
	for number in line_arr:
		if number != '':
			arr.append(int(number))
#get input complete

arr1 = list(arr)
arr2 = list(arr)

rselect_start = time.time()
rresult = rselect(arr1, nth)
rselect_end = time.time()
print("[Randomized select result]")
print(nth, "smallest element :", rresult)
print("program running time : %s" %round((rselect_end - rselect_start), 2)+"s")

dselect_start = time.time()
dresult = dselect(arr2, nth)
dselect_end = time.time()
print("[Deterministic select result]")
print(nth, "smallest element :", dresult)
print("program running time : %s" %round((dselect_end - dselect_start), 2)+"s")