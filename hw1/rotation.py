import random
import sys
import time

number = int(sys.argv[1])

test = []
for x in range(0, number):
	test.append(random.randrange(0, number*10))

start = time.time()
for x in range(0, number):
	pass
end = time.time()

print("running time : %s" %round((end - start), 3)+"s")