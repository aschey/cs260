from binarytree import BinaryTree
from binarynode import BinaryNode
from queuesll import QueueSLL
from stacksll import StackSLL
class HeapBT(object):
	def __init__(self):
		self.store = BinaryTree()
		self.stack = StackSLL()

	def readData(self, data):
		"""
		reads data from a queue and inserts it into the heap
		"""
		while not data.isEmpty():
			self.addNode(data.dequeue())

	def addNode(self, value):
		"""
		adds the node to the heap
		"""
		node = BinaryNode(value)
		self.store.add(node)
		self.stack.push(node)

	def heapify(self, current):
		"""
		makes the parent node and its children have the heap property
		"""
		swapNode = self.store.getMinChild(current)
		if swapNode != None:
			self.store.swapValues(swapNode, current)
			if swapNode.getLeft() != None or swapNode.getRight() != None:
				self.heapify(swapNode)

	def buildHeap(self):
		"""
		makes the entire tree into a heap
		"""
		if self.stack.isEmpty():
			raise ValueError("The tree is empty or the heap has already been built")
		i = 0
		while True:
			current = self.stack.pop()
			if current.getParent() == None:
				break
			if i % 2 == 0:
				self.heapify(current.getParent())
			i += 1

	def extractMin(self):
		"""
		returns the root node and restores the heap property on the rest of the tree
		"""
		root = self.store.getRoot()
		if root == None:
			return
		pruneNode = self.store.getLastNode()
		self.store.prune(pruneNode)
		self.store.swapValues(root, pruneNode)
		self.heapify(root)
		return pruneNode.getValue()

	def bubbleUp(self, current):
		"""
		moves the node up the tree until it is greater than the parent
		"""
		while True:
			parent = current.getParent()
			if parent != None and current < parent:
				self.store.swapValues(parent, current)
				current = parent
			else:
				break

	def insert(self, value):
		"""
		inserts the value into the correct location in the tree
		"""
		self.addNode(value)
		self.bubbleUp(self.store.getLastNode())

	def sort(self):
		"""
		performs a heapsort
		"""
		queue = QueueSLL()
		while True:
			minVal = self.extractMin()
			if minVal == None:
				break
			queue.enqueue(minVal)
		return queue

	def isCorrect(self):
		"""
		returns True if the tree is a heap
		"""
		queue = QueueSLL()
		queue.enqueue(self.store.getRoot())
		while not queue.isEmpty():
			current = queue.dequeue()
			incorrectNode = self.store.getMinChild(current)
			if self.store.getMinChild(current) != None:
				return False
			left = current.getLeft()
			if left != None:
				queue.enqueue(left)
			right = current.getRight()
			if right != None:
				queue.enqueue(right)
		return True

	def peek(self):
		"""
		returns the value at the root of the heap
		"""
		return self.store.getRoot()

	def isEmpty(self):
		"""
		returns true if the heap is empty
		"""
		# check root separately because size does not account for root
		return self.store.getSize() == 0 and self.store.getRoot() == None 

def main():
	heap = HeapBT()
	heap.readData([3,6,2,11,8,9,10])
	#print(heap.store.root.value)
	heap.buildHeap()
	heap.insert(2)
	#heap.insert(10)
	#heap.insert(1)
	stack = heap.store.levelOrderTraverse()
	while not stack.isEmpty():
		print(stack.pop().getValue())
	print(heap.isCorrect())
	#while not queue.isEmpty():
	#	print(queue.dequeue())
	

if __name__ == '__main__':
	main()
