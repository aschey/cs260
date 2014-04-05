from dynamicarray import DynamicArray
class Heap(object):
	def __init__(self, capacity):
		self.store = DynamicArray(capacity)
	
	def readArrayData(self, array):
		"""
		reads values from an array and inputs them into a fillable array
		"""
		for v in array:
			self.store.addToBack(v)

	def get(self, currentIndex):
		"""
		returns the value at the index
		"""
		return self.store.get(currentIndex)

	def getParentIndex(self, nodeIndex):
		"""
		returns the parent of the node
		"""
		# node is the root if its index is 0
		if nodeIndex > 0:
			return (nodeIndex - 1) // 2

	def getLeftChildIndex(self, nodeIndex):
		"""
		returns the left child of the node
		"""
		leftChildIndex = nodeIndex * 2 + 1
		if leftChildIndex < self.store.getSize():
			return leftChildIndex

	def getRightChildIndex(self, nodeIndex):
		"""
		returns the right child of the node
		"""
		rightChildIndex = nodeIndex * 2 + 2
		if rightChildIndex < self.store.getSize():
			return rightChildIndex

	def getMinChildIndex(self, parentIndex):
		"""
		returns the smallest child of the parent node, None if there is none
		"""
		leftIndex = self.getLeftChildIndex(parentIndex)
		rightIndex = self.getRightChildIndex(parentIndex)
		if leftIndex != None and self.store.get(leftIndex) < self.store.get(parentIndex) or \
				rightIndex != None and self.store.get(rightIndex) < self.store.get(parentIndex):
			if rightIndex == None:
				return leftIndex
			elif self.store.get(rightIndex) < self.store.get(leftIndex):
				return rightIndex
			else:
				return leftIndex

	def swapValues(self, index1, index2):
		"""
		swaps the values at index 1 and 2
		"""
		temp = self.store.get(index1)
		self.store.setAtIndex(index1, self.store.get(index2))
		self.store.setAtIndex(index2, temp)

	def prune(self, pruneIndex):
		"""
		removes the node from the array
		PRECONDITION: the node is a leaf
		"""
		self.store.removeFromIndex(pruneIndex)

	def heapify(self, currentIndex):
		"""
		makes the parent node and its children have the heap property
		"""
		swapIndex = self.getMinChildIndex(currentIndex)
		if swapIndex != None:
			self.swapValues(swapIndex, currentIndex)
			if self.getLeftChildIndex(swapIndex) != None or self.getRightChildIndex(swapIndex) != None:
				self.heapify(swapIndex)

	def buildHeap(self):
		"""
		makes the entire array into a heap
		"""
		currentIndex = self.store.getSize() - 1
		while currentIndex > 0:
			self.heapify(self.getParentIndex(currentIndex))
			currentIndex -= 2

	def extractMin(self):
		"""
		returns the root node and restores the heap property on the rest of the tree
		"""
		rootIndex = 0
		rootValue = self.store.get(rootIndex)
		pruneIndex = self.store.getSize()-1
		self.store.setAtIndex(rootIndex, self.store.get(pruneIndex))
		self.prune(pruneIndex)
		self.heapify(rootIndex)
		return rootValue

	def bubbleUp(self, currentIndex):
		"""
		moves the node up the tree until it is greater than the parent
		"""
		while True:
			parentIndex = self.getParentIndex(currentIndex)
			if self.store.get(currentIndex) < self.store.get(parentIndex):
				self.swapValues(currentIndex, parentIndex)
				currentIndex = parentIndex
			else:
				break

	def insert(self, value):
		"""
		inserts the node into the correct place in the heap
		"""
		self.store.addToBack(value)
		self.bubbleUp(self.store.getSize()-1)

	def peek(self):
		"""
		returns the value at the root of the heap
		"""
		return self.store.get(0)

	def isEmpty(self):
		"""
		returns true if the heap is isEmpty
		"""
		return self.store.getSize() == 0

def main():
	heap = Heap(10)
	#heap.readArrayData([4,2,6,1,4,3,7,8,5,6])
	heap.readArrayData([1,2,3,4,4,6,7,8,5,6])
	#heap.readArrayData([6,4,3,2,4,6,7,8,5])
	#heap.buildHeap()
	#for i in range(heap.store.size):
	#	print(heap.store.get(i))
	for i in range(heap.store.size):
		print(heap.extractMin())

if __name__ == '__main__':
	main()