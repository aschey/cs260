from queuesll import QueueSLL
from binarynode import BinaryNode 
from stacksll import StackSLL
from queuesll import QueueSLL
class BinaryTree(object):
	def __init__(self):
		self.root = None
		self.size = 0

	def add(self, value):
		"""
		adds the value to the bottom of the tree
		"""
		node = BinaryNode(value)
		if self.root == None:
			self.root = node
		else:
			self.size += 1
			queue = QueueSLL()
			queue.enqueue(self.root)
			while not queue.isEmpty():
				current = queue.dequeue()
				if current.getLeft() != None:
					queue.enqueue(current.getLeft())
				else:
					self.setLeftChild(current, node)
					break
				if current.getRight() != None:
					queue.enqueue(current.getRight())
				else:
					self.setRightChild(current, node)
					break

	def levelOrderTraverse(self):
		"""
		performs a level-order traverse and returns a stack of the nodes
		"""
		queue = QueueSLL()
		stack = StackSLL()
		queue.enqueue(self.root)
		while not queue.isEmpty():
			current = queue.dequeue()
			stack.push(current)
			if current.getLeft() != None:
				queue.enqueue(current.getLeft())
			if current.getRight() != None:
				queue.enqueue(current.getRight())
		return stack

	def getLastNode(self):
		"""
		returns the last node in the tree
		"""
		nodesInLevel = 2
		remainingNodes = self.size
		while remainingNodes > 0:
			remainingNodes -= nodesInLevel
			nodesInLevel *= 2
		position = remainingNodes + nodesInLevel // 2
		current = self.root
		positionCheck = nodesInLevel // 2
		while positionCheck > 1:
			positionCheck //= 2
			if position <= positionCheck:
				current = current.getLeft()
			else:
				current = current.getRight()
				position -= positionCheck
		return current


	def swapValues(self, node1, node2):
		"""
		swaps the values of node1 and node2
		"""
		val1 = node1.getValue()
		val2 = node2.getValue()
		node1.setValue(val2)
		node2.setValue(val1)

	def getMinChild(self, node):
		"""
		returns the min child of the node, None if the parent is the min
		"""
		left = node.getLeft()
		right = node.getRight()
		if left != None and left.getValue() < node.getValue() or \
				right != None and right.getValue() < node.getValue():
			if right == None:
				return left
			elif right.getValue() < left.getValue():
				return right
			else:
				return left

	def prune(self, node):
		"""
		removes the node from the tree
		PRECONDITION: the node is a leaf
		"""
		if node.getParent() != None:
			if node.isLeftChild():
				node.getParent().setLeft(None)
			else:
				node.getParent().setRight(None)
		else:
			self.root = None
		node.setParent(None)
		self.size -= 1

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
	bt.add(3)
	bt.add(4)
	bt.add(5)
	bt.add(1)
	bt.add(10)
	bt.add(11)
	bt.add(3)
	bt.add(4)
	bt.add(24)
	bt.add(34)
	bt.add(100)
	bt.add(1000)
	bt.add(1)
	bt.add(2)
	bt.add(3)
	bt.add(4)
	bt.add(5)

	print(bt.getLastNode().getValue())

if __name__ == '__main__':
	main()

		