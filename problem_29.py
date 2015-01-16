#problem 29

#create a two dimensions array
arr = [[1 for x in xrange (99)] for y in xrange(99)]

for i in range (99):
	for j in range (99):
		for k in range (1, 100):
			if (((i + 2) ** (k + 1) <= 100) and ((j + 2) % (k + 1) == 0) and ((j + 2) / (k + 1) >= 2)):
				arr [(i + 2) ** (k + 1) - 2][(j + 2) / (k + 1) - 2] = 0
				print str((i + 2) ** (k + 1)) + " " + str ((j + 2) / (k + 1))

count = 0
for i in range (99):
	for j in range (99):
		if arr[i][j] == 1:
			count += 1

print count