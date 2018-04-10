import random
import sys

number = int(sys.argv[1])

test = []
for x in range(0, number+1):
	test.append(random.randrange(0, number*10))

for x in range(1, number+1):
	print(str(test[x]) + " ", end='')
	if(x%19 == 0 and x != 0):
		print('')