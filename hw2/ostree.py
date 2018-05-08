BLACK = 0
RED = 1

class Node:
	color = None
	data = None
	parent = None
	left = None
	right = None
	size = None
	def __init__(self, x):
		self.data = x
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

leafNode = Node(None)
leafNode.setColor(BLACK)

def insert(head, x):
	newNode = Node(x)
	newNode.setSize(1)
	newNode.left = leafNode
	newNode.right = leafNode
	if head.data == None:
		head.setData(x)
		head.setSize(1)
	else:
		curr = head
		while True:
			if x < curr.data:
				if curr.left != None:
					curr.setSize(curr.size+1)
					curr = curr.left
				else:
					curr.setSize(curr.size+1)
					newNode.setParent(curr)
					curr.setLeft(newNode)
					insert_case1(newNode)
					break
			else:
				if curr.right != None:
					curr.setSize(curr.size+1)
					curr = curr.right
				else:
					curr.setSize(curr.size+1)
					newNode.setParent(curr)
					curr.setRight(newNode)
					insert_case1(newNode)
					break

def insert_case1(n):
	if n.parent == None:
		n.setColor(BLACK)
	else:
		insert_case2(n)

def insert_case2(n):
	if n.parent.color == BLACK:
		return;
	else:
		insert_case3(n)

def insert_case3(n):
	u = n.getUncle()

	if u != None and u.color == RED:
		

head = Node(None)
head.left = leafNode
head.right = leafNode

