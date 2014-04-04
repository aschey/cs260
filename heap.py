from fillablearray import FillableArray
class Heap(object):
	def __init__(self, capacity):
		self.store = FillableArray(capacity)
	
	def readArrayData(self, array):
		"""
		reads values from an array and inputs them into a fillable array
		"""
		for v in array:
			self.store.addToBack(v)

	def getParentIndex(self, nodeIndex):
		"""
		returns the parent of the node
		"""
		# node is the root if its index is 0
		if nodeIndex > 0:
			return nodeIndex // 2

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
			if rightIndex != None:
				return leftIndex
			elif leftIndex != None or self.store.get(rightIndex) < self.store.get(leftIndex):
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
				self.heapify(currentIndex)

	def buildHeap(self):
		"""
		makes the entire array into a heap
		"""
		currentIndex = self.store.getSize() - 1
		while True:
			if currentIndex == 0:
				break
			self.heapify(self.getParentIndex(currentIndex))
			currentIndex -= 1

	def extractMin(self):
		"""
		returns the root node and restores the heap property on the rest of the tree
		"""
		rootIndex = 0
		pruneIndex = self.store.getSize()-1
		self.store.setAtIndex(rootIndex, self.store.get(pruneIndex))
		self.prune(pruneIndex)
		self.heapify(rootIndex)

def main():
	heap = Heap(10)
	heap.readArrayData([4,2,6,1,4,3,7,8,5])
	heap.buildHeap()
	for i in range(heap.store.size):
		print(heap.store.get(i))

if __name__ == '__main__':
	main()