# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:  
    def serialize(self, root):
        # get a preorder traversal string
        res = []

        def preOrder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ",".join(res)
        

    def deserialize(self, data):
        dataList = data.split(",")

        self.ptr = 0

        def preOrderConstruct():
            if dataList[self.ptr] == "N":
                self.ptr += 1
                return None
            
            node = TreeNode(int(dataList[self.ptr]))
            self.ptr += 1
            node.left = preOrderConstruct()
            node.right = preOrderConstruct()
            return node
        
        return preOrderConstruct()