# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes = dict()

        for d in descriptions:
            val, child, isLeft = d

            if val not in nodes:
                if isLeft:  nodes[val] = [None, child, None]
                else:       nodes[val] = [None, None, child]
            else:
                if isLeft:  nodes[val][1] = child
                else:       nodes[val][2] = child

        for node_val in nodes:
            n = nodes[node_val]
            parent, left, right = n
            if left is not None and left in nodes:
                nodes[left][0] = node_val
            if right is not None and right in nodes:
                nodes[right][0] = node_val

        root = None
        for node_val in nodes:
            node = nodes[node_val]
            if node[0] is None:
                root = node_val
                break

        def createBinaryTreeFromDict(node_val):
            if node_val in nodes:
                left = nodes[node_val][1]
                right = nodes[node_val][2]
            else: left, right = None, None
            left_node, right_node = None, None
            if left is not None: left_node = createBinaryTreeFromDict(left)
            if right is not None: right_node = createBinaryTreeFromDict(right)
            node = TreeNode(node_val, left_node, right_node)
            return node

        tree_root = createBinaryTreeFromDict(root)

        return tree_root
