from dynamicarray import DynamicArray
class Heap(object):
	def __init__(self, capacity):
		self.store = DynamicArray(capacity)
		self.ROOT_INDEX = 0
		self.size = 0
	
	def readData(self, array):
		"""
		reads values from an array and inputs them into a fillable array
		"""
		for v in array:
			self.store.addToBack(v)
			self.size += 1

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

	def getLeftIndex(self, nodeIndex):
		"""
		returns the left child of the node
		"""
		leftChildIndex = nodeIndex * 2 + 1
		if leftChildIndex < self.size:
			return leftChildIndex

	def getRightIndex(self, nodeIndex):
		"""
		returns the right child of the node
		"""
		rightChildIndex = nodeIndex * 2 + 2
		if rightChildIndex < self.size:
			return rightChildIndex

	def getMaxIndex(self, parentIndex):
		"""
		returns the smallest child of the parent node, None if there is none
		"""
		leftIndex = self.getLeftIndex(parentIndex)
		rightIndex = self.getRightIndex(parentIndex)
		if leftIndex != None and self.store.get(leftIndex) > self.store.get(parentIndex) or \
				rightIndex != None and self.store.get(rightIndex) > self.store.get(parentIndex):
			if rightIndex == None:
				return leftIndex
			elif self.store.get(rightIndex) > self.store.get(leftIndex):
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
		swapIndex = self.getMaxIndex(currentIndex)
		if swapIndex != None:
			self.swapValues(swapIndex, currentIndex)
			if self.getLeftIndex(swapIndex) != None or self.getRightIndex(swapIndex) != None:
				self.heapify(swapIndex)

	def buildHeap(self):
		"""
		makes the entire array into a heap
		"""
		currentIndex = self.store.getSize() - 1
		while currentIndex > 0:
			self.heapify(self.getParentIndex(currentIndex))
			currentIndex -= 2

	def extractMax(self):
		"""
		returns the root node and restores the heap property on the rest of the tree
		"""
		rootValue = self.store.get(self.ROOT_INDEX)
		self.size -= 1
		self.swapValues(self.ROOT_INDEX, self.size)
		self.heapify(self.ROOT_INDEX)

	def sort(self):
		"""
		sorts the heap in ascending order
		"""
		for i in range(self.store.getSize()):
			self.extractMax()
		self.size = self.store.getSize()
		

	def bubbleUp(self, currentIndex):
		"""
		moves the node up the tree until it is greater than the parent
		"""
		while True:
			parentIndex = self.getParentIndex(currentIndex)
			if parentIndex != None and self.store.get(currentIndex) > self.store.get(parentIndex):
				self.swapValues(currentIndex, parentIndex)
				currentIndex = parentIndex
			else:
				break

	def insert(self, value):
		"""
		inserts the node into the correct place in the heap
		"""
		self.store.addToBack(value)
		self.size += 1
		self.bubbleUp(self.size-1)

	def peek(self):
		"""
		returns the value at the root of the heap
		"""
		if not self.store.isEmpty():
			return self.store.get(0)

	def isEmpty(self):
		"""
		returns true if the heap is isEmpty
		"""
		return self.store.getSize() == 0

def main():
	heap = Heap(10)
	heap.readData([3,4,1,6,8,2,3,8,5])
	heap.buildHeap()
	heap.insert(5)
	heap.insert(10)
	#heap.extractMax()
	#heap.store = DynamicArray(10)
	#for i in [7,6,6,5,4,1,3,4,2,8]:
	#	heap.store.addToBack(i)
	#heap.size = 9
	heap.sort()
	for i in range(heap.store.size):
	   print(heap.store.get(i))
	# heap.sort()
	# for i in range(heap.store.size):
	# 	print(heap.store.get(i))

if __name__ == '__main__':
	main()