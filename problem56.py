import time

start_time = time.clock ()

def sumDigits (n):
	res = 0
	for d in str (n):
		res += int (d)
	return res

max_total = 0

for a in range (1, 100):
	for b in range (1, 100):
		total_digit = sumDigits (a ** b)
		if (total_digit > max_total):
			max_total = total_digit

print max_total

print time.clock () - start_time, " seconds"