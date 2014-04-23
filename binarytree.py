from binarynode import BinaryNode 
from stacksll import StackSLL
from queuesll import QueueSLL
class BinaryTree(object):
	def __init__(self):
		self.root = None
		self.store = StackSLL()

	def add(self, node, parent):
		"""
		adds the value to the bottom of the tree
		"""
		self.store.push(node)
		if self.root == None:
			self.root = node
		else:
			if parent.getLeft() == None:
				self.setLeftChild(parent, node)
			else:
				self.setRightChild(parent, node)

	def getLastNode(self):
		"""
		returns the last node in the tree
		"""
		return self.store.peek()

	def swapValues(self, node1, node2):
		"""
		swaps the values of node1 and node2
		"""
		val1 = node1.getValue()
		val2 = node2.getValue()
		node1.setValue(val2)
		node2.setValue(val1)

	def getMinChild(self, parent):
		"""
		returns the min child of the node, None if the parent is the min
		"""
		left = parent.getLeft()
		right = parent.getRight()
		# if the node has at least one child less than it
		if self._lessThan(left, parent) or self._lessThan(right, parent):
			if right == None:
				return left
			elif right < left:
				return right
			else:
				return left

	def _lessThan(self, node1, node2):
		"""
		returns True if node1 is less than node2
		PRECONDITION: node2 can NOT be a child of node1
		"""
		return node1 != None and node1 < node2

	def prune(self, node):
		"""
		removes the node from the tree
		PRECONDITION: the node is a leaf
		"""
		parent = node.getParent()
		if parent != None:
			if node.isLeftChild():
				self.setLeftChild(parent, None)
			else:
				self.setRightChild(parent, None)
		else:
			self.root = None
		self.store.pop()

	def setLeftChild(self, parent, child):
		"""
		sets the child as the left node of the parent
		"""
		parent.setLeft(child)
		if child != None:
			child.setParent(parent)

	def setRightChild(self, parent, child):
		"""
		sets the child as the right node of the parent
		"""
		parent.setRight(child)
		if child != None:
			child.setParent(parent)

	def getRoot(self):
		"""
		returns the root of the tree
		"""
		return self.root

def main():
	bt = BinaryTree()
	bt.add(BinaryNode(3))
	bt.add(BinaryNode(4))
	bt.add(BinaryNode(5))
	bt.add(BinaryNode(6))
	bt.add(BinaryNode(7))
	bt.add(BinaryNode(8))
	print(bt.root.right.left.value)

if __name__ == '__main__':
	main()

		
