import time

start_time = time.clock ()

total = 0

for i in range (1, 1001):
	total += ((i ** i) % 10000000000)

print total % 10000000000

print time.clock() - start_time, "seconds"