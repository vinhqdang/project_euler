coins = [200, 100, 50, 20, 10, 5, 2, 1]

count = 0

trace = list ()

TARGET = 200

class Node:
	def __init__ (self, current_value, current_index, bags):
		self.current_value = current_value
		self.current_index = current_index
		self.bags = bags
		if (self.bags is None):
			self.bags = list ()
			self.bags.append (1)
			self.bags.append (2)
		#print ('***')
		#print self.bags
	def value (self):
		return self.current_value
	def bags (self):
		return self.bags
	def left (self):
		if (self.current_value + coins [self.current_index] > TARGET):
			return None
		#print coins [self.current_index]
		left_bags = list()
		left_bags += self.bags
		left_bags.append (coins [self.current_index])
		#print left_bags
		#print '----'
		return Node (self.current_value + coins [self.current_index], self.current_index, left_bags)
	def right (self):
		right_bags = list ()
		right_bags += self.bags
		if (self.current_index < len (coins) - 1):
			return Node (self.current_value, self.current_index + 1, right_bags)
		elif (self.current_value < TARGET):
			return Node (self.current_value, self.current_index, right_bags)
		else:
			return None

root_bags = list ()
root = Node (0, 0, root_bags)
trace.append (root)

while (len(trace) != 0):
	#current_node = trace [0]
	left = trace[0].left ()
	if (left is not None):
		trace.append (trace [0].left ())
	right = trace [0].right ()
	if (right is not None):
		trace.append (trace [0].right ())
	if (trace [0].value () == TARGET):
		count += 1
		print str(count)
		print trace[0].bags
		#for j in range (len (trace[0].bags)):
			#print trace[0].bags[j]
		#print '---'
	trace.pop (0)

print count