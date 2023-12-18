from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



def preorder_traversal(root: Optional[Node]) -> List[int]:
    ...
