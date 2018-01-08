import DataStructures.BinaryTree as bt

tree = bt.BinaryTree()

# Duplicates in the array are not supported
def insertIntoTree(arr):
      for num in arr:
            node = tree.insertNode(num)
            node.index = arr.index(num)

def Heapify(tree):
      # find the max, replace it with the root, and swap the array index as well
      pass
      

insertIntoTree([1,2,4,42,3]) 
print(tree.getChild(tree.root))
