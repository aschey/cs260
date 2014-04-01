from queuesll import QueueSLL
from binarynode import BinaryNode 
class BinaryTree(object):
	def __init__(self):
		self.root = None

	def add(self, value):
		"""
		adds the value to the bottom of the tree
		"""
		node = BinaryNode(value)
		if self.root == None:
			self.root = node
		else:
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
		
	def delete(self, value):
		pass

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

def main():
	bt = BinaryTree()
	bt.add(3)
	bt.add(4)
	bt.add(5)
	bt.add(1)
	bt.add(10)
	print(bt.root.left.right.value)

if __name__ == '__main__':
	main()

		