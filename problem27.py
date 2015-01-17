import math
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def calcQuadratic (n, a, b):
	return n * n + n * a + b

max_consecutive = 0
max_a = -1000
max_b = -1000
for a in range (-999, 1000):
	for b in range (-999, 1000):
		n = 0
		while (True):
			if (is_prime (calcQuadratic (n, a, b))):
				n += 1
			else:
				break
		if (n > max_consecutive):
			max_consecutive = n
			max_a = a
			max_b = b

print max_a
print max_b
print max_consecutive
print max_a * max_b