from math import factorial
import time

start_time = time.clock()

def checkFactorialDigits (n):
	res = 0
	number = n
	while (number != 0):
		digit = number % 10
		number = number / 10
		res += factorial (digit)
	if (res == n):
		return True
	else:
		return False

total = 0

for i in range (3, 10000000):
	if (checkFactorialDigits (i)):
		print i
		total += i

print total

print time.clock() - start_time, "seconds"
