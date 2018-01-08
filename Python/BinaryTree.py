class BinaryNode:
      def __init__(self, val):
            self.val   = val
            self.right = None
            self.left  = None

class BinaryTree:
      def __init__(self):
            self.root = None
      
      def getRoot(self):
            return self.root
      
      def insertNode(self, val):
            if(self.root == None):
                  self.root = BinaryNode(val)
            
            else:
                  self._insertNode(val, self.root)
      
      # Simple overloading method
      def _insertNode(self, val, node):
            if(val < node.val):
                  if(node.left == None):
                        node.left = BinaryNode(val)
                  else:
                        self._insertNode(val, node.left)
            
            if(val > node.val):
                  if(node.right == None):
                        node.right = BinaryNode(val)
                  else:
                        self._insertNode(val, node.right)
            
      def find(self, val, node='root'):
            if (node is 'root'):
                  node = self.root
            if (node.val):
                  return False
            elif (node.val == val):
                  return True
            elif (node.val > val):
                  return self.find(val, node.left)
            elif (node.val < val):
                  return self.find(val, node.right)
      
      def getChild(self, node):
            if (not node):
                  return ""
            if (not node.right and not node.left):
                  return str(node.val)
            else:
                  return self.getChild(node.left) + "-" + str(node.val)+ "-" + self.getChild(node.right)

def main():
      tree = BinaryTree()
      tree.insertNode(5)
      tree.insertNode(4)
      tree.insertNode(2)
      tree.insertNode(6)
      tree.insertNode(7)
      tree.insertNode(6)
      print(tree.find(54))
      print("Print in order: ",tree.getChild(tree.root), "\nThe root is: ", tree.root.val)



main()