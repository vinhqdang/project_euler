import time

from math import factorial

start_time = time.clock ()

count = 0

def combine (n, r):
	return factorial (n) / factorial (r) / factorial (n - r)

for n in range (1, 101):
	for r in range (1, n):
		if (combine (n, r) > 1000000):
			count += 1

print count

print time.clock () - start_time, "seconds"