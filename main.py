#!/usr/bin/env python3

import math
import sys
from collections import defaultdict
from treeutil import parse_tree
from treeutil import tree_to_arr


class Solver:
    def __init__(self):
        pass

    def solve(self, root, to_delete):
        stack = [(root, True)]
        rv = []

        while len(stack) != 0:
            node, is_root = stack.pop()
            if node is None:
                pass
            elif node.val in to_delete:
                stack += [(node.left, True), (node.right, True)]
            else:
                if is_root:
                    rv.append(node)
                stack += [(node.left, False), (node.right, False)]
                if node.left is not None and node.left.val in to_delete:
                    node.left = None
                if node.right is not None and node.right.val in to_delete:
                    node.right = None
        return rv



if __name__ == '__main__':
    solver = Solver()
    tree_arr = [1,2,3,4,5,6,7]
    tree = parse_tree(tree_arr)
    to_delete = [3, 5]

    r = solver.solve(tree, to_delete)
    for t in r:
        print(tree_to_arr(t))
