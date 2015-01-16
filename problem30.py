total_sum = 0

for i in range (2, 1000000):
	num = i
	sum_digit = 0
	while (num != 0):
		digit = num % 10
		num = num / 10
		sum_digit += digit ** 5
	if (sum_digit == i):
		print i
		total_sum += sum_digit

print total_sum