from binarytree import BinaryTree
from binarynode import BinaryNode
from queuesll import QueueSLL
from stacksll import StackSLL
class HeapBT(object):
	def __init__(self):
		self.store = BinaryTree()

	def readTreeData(self, data):
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
		root = self.store.getRoot()
		pruneNode = self.store.getLastNode()
		self.store.prune(pruneNode)
		self.store.swapValues(root, pruneNode)
		self.heapify(root)
		return pruneNode.getValue()

	def peek(self):
		return self.store.getRoot()

	def isEmpty(self):
		"""
		returns true if the heap is isEmpty
		"""
		# check root separately because size does not account for root
		return self.store.getSize() == 0 and self.store.getRoot() == None 

def main():
	heap = HeapBT()
	heap.readTreeData([1,3,6,10,11,1,8,9])
	#print(heap.store.root.value)
	heap.buildHeap()
	for i in range(heap.store.size+1):
		print(heap.extractMin())
	

if __name__ == '__main__':
	main()