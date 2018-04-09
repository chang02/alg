import random
import sys

number = int(sys.argv[1])

test = []
for x in range(0, number):
	test.append(random.randrange(0, number*10))

for x in range(0, number):
	print(str(test[x]) + " ", end='')