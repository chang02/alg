BLACK = 0
RED = 1
import sys

class Node:
	color = None
	data = None
	parent = None
	left = None
	right = None
	size = None
	def __init__(self, x):
		self.data = x
		self.color = RED
	def setColor(self, c):
		self.color = c
	def setData(self, x):
		self.data = x
	def setParent(self, n):
		self.parent = n
	def setLeft(self, l):
		self.left = l
	def setRight(self, r):
		self.right = r
	def setSize(self, s):
		self.size = s
	def getGrandparent(self):
		if self != None and self.parent!= None:
			return self.parent.parent
		else:
			return None
	def getUncle(self):
		g = self.getGrandparent()
		if g == None:
			return None
		if self.parent == g.left:
			return g.right
		else:
			return g.left
	def getSibling(self):
		if self == self.parent.left:
			return self.parent.right
		else:
			return self.parent.left

class ostree:
	head = None
	def insert(self, x):
		newLeaf1 = Node(None)
		newLeaf1.setColor(BLACK)
		newLeaf1.setSize(0)
		newLeaf2 = Node(None)
		newLeaf2.setColor(BLACK)
		newLeaf2.setSize(0)
		

		newNode = Node(x)
		newNode.setSize(1)
		newNode.setLeft(newLeaf1)
		newNode.setRight(newLeaf2)
		newLeaf1.setParent(newNode)
		newLeaf2.setParent(newNode)
		newNode.setColor(RED)

		if self.head == None:
			self.head = newNode
			self.insert_case1(self.head)
			return x
		else:
			curr = self.head
			while True:
				if x == curr.data:
					if curr == self.head:
						return 0
					else:
						curr = curr.parent
						while curr != self.head:
							curr.setSize(curr.size - 1)
							curr = curr.parent
						self.head.setSize(self.head.size - 1)
						return 0
				elif x < curr.data:
					if curr.left.data != None:
						curr.setSize(curr.size+1)
						curr = curr.left
					else:
						curr.setSize(curr.size+1)
						newNode.setParent(curr)
						curr.setLeft(newNode)
						self.insert_case1(newNode)
						return x
				else:
					if curr.right.data != None:
						curr.setSize(curr.size+1)
						curr = curr.right
					else:
						curr.setSize(curr.size+1)
						newNode.setParent(curr)
						curr.setRight(newNode)
						self.insert_case1(newNode)
						return x

	def insert_case1(self, n):
		if n.parent == None:
			n.setColor(BLACK)
		else:
			self.insert_case2(n)

	def insert_case2(self, n):
		if n.parent.color == BLACK:
			return;
		else:
			self.insert_case3(n)

	def insert_case3(self, n):
		u = n.getUncle()

		if u.data != None and u.color == RED:
			n.parent.setColor(BLACK)
			u.setColor(BLACK)
			g = n.getGrandparent()
			g.setColor(RED)
			self.insert_case1(g)
		else:
			self.insert_case4(n)

	def insert_case4(self, n):
		g = n.getGrandparent()
		if n == n.parent.right and n.parent == g.left:
			self.rotate_left(n.parent)
			n = n.left
		elif n == n.parent.left and n.parent == g.right:
			self.rotate_right(n.parent)
			n = n.right
		self.insert_case5(n)

	def insert_case5(self, n):
		g = n.getGrandparent()
		n.parent.setColor(BLACK)
		g.setColor(RED)
		if n == n.parent.left:
			self.rotate_right(g)
		else:
			self.rotate_left(g)

	def rotate_left(self, n):
		c = n.right
		p = n.parent

		c.setSize(n.size)
		n.setSize(c.left.size + n.left.size + 1)

		if c.left.data != None:
			c.left.setParent(n)

		n.setRight(c.left)
		n.setParent(c)
		c.setLeft(n)
		c.setParent(p)

		if p != None:
			if p.left == n:
				p.setLeft(c)
			else:
				p.setRight(c)
		else:
			self.head = self.head.parent


	def rotate_right(self, n):
		c = n.left
		p = n.parent

		c.setSize(n.size)
		n.setSize(c.right.size + n.right.size + 1)

		if c.right.data != None:
			c.right.setParent(n)

		n.setLeft(c.right)
		n.setParent(c)
		c.setRight(n)
		c.setParent(p)

		if p != None:
			if p.right == n:
				p.setRight(c)
			else:
				p.setLeft(c)
		else:
			self.head = self.head.parent

	def delete(self, x):
		curr = self.head
		targetNode = None
		leastNode = None
		if self.head == None:
			return 0
		if self.head.data == x and self.head.left.data == None and self.head.right.data == None:
			self.head = None
			return x
		while curr.data != None:
			if curr.data == x:
				targetNode = curr
				break
			elif curr.data < x:
				curr = curr.right
			elif curr.data > x:
				curr = curr.left

		if curr.data == None:
			return 0

		if targetNode.right.data == None:
			leastNode = targetNode
		else:
			curr = targetNode.right
			while curr.left.data != None:
				curr = curr.left
			leastNode = curr

		curr = leastNode
		while curr != self.head:
			curr.setSize(curr.size - 1)
			curr = curr.parent
		self.head.setSize(self.head.size - 1)

		tempdata = targetNode.data
		targetNode.setData(leastNode.data)
		leastNode.setData(tempdata)

		self.delete_one_child(leastNode)
		return x

	def delete_one_child(self, n):
		child = None
		p = n.parent
		if n.right.data == None:
			child = n.left
		else:
			child = n.right

		if p == None:
			child.setParent(None)
			self.head = child
		elif n == p.left:
			p.setLeft(child)
			child.setParent(p)
		elif n == p.right:
			p.setRight(child)
			child.setParent(p)

		if n.color == BLACK:
			if child.color == RED:
				child.setColor(BLACK)
			else:
				self.delete_case1(child)
	def delete_case1(self, n):
		if n.parent != None:
			self.delete_case2(n)
	def delete_case2(self, n):
		s = n.getSibling()
		if s.color == RED:
			n.parent.setColor(RED)
			s.setColor(BLACK)
			if n == n.parent.left:
				self.rotate_left(n.parent)
			else:
				self.rotate_right(n.parent)
		self.delete_case3(n)
	def delete_case3(self, n):
		s = n.getSibling()
		if n.parent.color == BLACK and s.color == BLACK and s.left.color == BLACK and s.right.color == BLACK:
			s.setColor(RED)
			self.delete_case1(n.parent)
		else:
			self.delete_case4(n)
	def delete_case4(self, n):
		s = n.getSibling()
		if n.parent.color == RED and s.color == BLACK and s.left.color == BLACK and s.right.color == BLACK:
			s.setColor(RED)
			n.parent.setColor(BLACK)
		else:
			self.delete_case5(n)
	def delete_case5(self, n):
		s = n.getSibling()
		if s.color == BLACK:
			if n == n.parent.left and s.right.color == BLACK and s.left.color == RED:
				s.setColor(RED)
				s.left.setColor(BLACK)
				self.rotate_right(s)
			elif n == n.parent.right and s.left.color == BLACK and s.right.color == RED:
				s.setColor(RED)
				s.right.setColor(BLACK)
				self.rotate_left(s)
		self.delete_case6(n)
	def delete_case6(self, n):
		s = n.getSibling()
		s.setColor(n.parent.color)
		n.parent.setColor(BLACK)

		if n == n.parent.left:
			s.right.setColor(BLACK)
			self.rotate_left(n.parent)
		else:
			s.left.setColor(BLACK)
			self.rotate_right(n.parent)

	def select(self, x, i):
		if self.head == None:
			return 0
		r = x.left.size + 1
		if i == r:
			return x.data
		elif i < r:
			if x.left.data == None:
				return 0
			else:
				return self.select(x.left, i)
		else:
			if x.right.data == None:
				return 0
			else:
				return self.select(x.right, i-r)

	def rank(self, x):
		if self.head == None:
			return 0

		curr = self.head
		while curr.data != None:
			if curr.data == x:
				break
			elif curr.data < x:
				curr = curr.right
			else:
				curr = curr.left

		if curr.data == None:
			return 0
			
		r = curr.left.size + 1
		y = curr
		while y != self.head:
			if y == y.parent.right:
				r = r + y.parent.left.size + 1
			y = y.parent
		return r

	def print_tree(self, node, blank):
		if not(node.data == None or node == None):
			print(blank + str(node.data))
			self.print_tree(node.left, blank + " ")
			self.print_tree(node.right, blank + " ")

t = ostree()
filename = sys.argv[1]

f = open(filename, 'r')
f2 = open("out.txt", 'w')
lines = f.readlines()

for line in lines:
	f2.write(line)

f2.write('\n')

for line in lines:
	i_arr = line.split(' ')
	command = i_arr[0]
	number = int(i_arr[1])
	if command == 'I':
		f2.write(str(t.insert(number)) + '\n')
	elif command == 'D':
		f2.write(str(t.delete(number)) + '\n')
	elif command == 'S':
		f2.write(str(t.select(t.head, number)) + '\n')
	elif command == 'R':
		f2.write(str(t.rank(number)) + '\n')
	elif command == 'P':
		t.print_tree(t.head, '')

f.close()
f2.close()