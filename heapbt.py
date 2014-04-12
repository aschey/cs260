from binarytree import BinaryTree
from binarynode import BinaryNode
from queuesll import QueueSLL
from stacksll import StackSLL
class HeapBT(object):
	def __init__(self):
		self.store = BinaryTree()

	def readData(self, data):
		for v in data:
			self.store.add(v)

	def heapify(self, current):
		swapNode = self.store.getMinChild(current)
		if swapNode != None:
			self.store.swapValues(swapNode, current)
			if swapNode.getLeft() != None or swapNode.getRight() != None:
				self.heapify(swapNode)

	def buildHeap(self):
		stack = self.store.levelOrderTraverse()
		i = 0
		while True:
			current = stack.pop()
			if current.getParent() == None:
				break
			if i % 2 == 0:
				self.heapify(current.getParent())
			i += 1

	def extractMin(self):
		# PRIORITY QUEUES
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
		self.store.add(value)
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

	def getIncorrectNode(self):
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
		return self.store.getRoot()

	def isEmpty(self):
		"""
		returns true if the heap is empty
		"""
		# check root separately because size does not account for root
		return self.store.getSize() == 0 and self.store.getRoot() == None 

def main():
	heap = HeapBT()
	heap.readData([3,6,2,11,8,9])
	#print(heap.store.root.value)
	#heap.buildHeap()
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