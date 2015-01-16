res = list ()

for i in range (2, 101):
	for j in range (2, 101):
		a = i ** j
		if a not in res:
			res.append (a)

print len(res)