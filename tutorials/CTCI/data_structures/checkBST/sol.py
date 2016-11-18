""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check_binary_search_tree_(root):
    return check_bounded(root)

def check_bounded(root, min = -float('inf'), max = float('inf')):
    if not root:
        return True
    return min < root.data < max and check_bounded(root.left, min, root.data) and check_bounded(root.right, root.data, max)
