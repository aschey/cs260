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
		swapNode = self._getMin(current)
		if swapNode != None:
			self.swapValues(swapNode, current)
			if swapNode.getLeft() != None or swapNode.getRight() != None:
				self.heapify(swapNode)

	def swapValues(self, node1, node2):
		"""
		swaps the values of node1 and node2
		"""
		val1 = node1.getValue()
		val2 = node2.getValue()
		print(val1, val2)
		node1.setValue(val2)
		node2.setValue(val1)


	def _getMin(self, node):
		"""
		returns the min child of the node
		"""
		left = node.getLeft()
		right = node.getRight()
		if (left != None and left.getValue() < node.getValue()) or (right != None and right.getValue() < node.getValue()):
			if right == None:
				return left
			elif left == None or right.getValue() < left.getValue():
				return right
			else:
				return left

	def buildHeap(self):
		stack = self.levelOrderTraverse()
		while True:
			current = stack.pop()
			if current.getParent() == None:
				break
			#print(current.getParent().getValue())
			self.heapify(current.getParent())
			stack.pop()

	def levelOrderTraverse(self):
		"""
		performs a level-order traverse and returns a stack of the nodes
		"""
		queue = QueueSLL()
		stack = StackSLL()
		queue.enqueue(self.store.root)
		while not queue.isEmpty():
			current = queue.dequeue()
			stack.push(current)
			if current.getLeft() != None:
				queue.enqueue(current.getLeft())
			if current.getRight() != None:
				queue.enqueue(current.getRight())
		return stack

	def getParent(self):
		pass

	def getLeftChild(self):
		pass

	def getRightChild(self):
		pass

	def extractMin(self):
		pass

	def bubbleUp(self):
		pass

	def insert(self, value):
		pass

	def peak(self):
		pass

	def isEmpty(self):
		pass

def main():
	heap = HeapBT()
	heap.readTreeData([1,3,6,3,8,6,4,2,4])
	#print(heap.store.root.value)
	heap.buildHeap()
	#print(heap.store.root.left.left.right.value)
	print(heap.store.root.right.right.value)

if __name__ == '__main__':
	main()