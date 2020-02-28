#!/usr/bin/env python3
"""
This is a utility function that converts between tree structure and its array-based notation,
which is commonly seen it leetcode problems.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def append_children_to_tree(root, arr, depth):
    print(root, arr, depth)
    if depth == 1:
        root.left = TreeNode(arr[0])
        root.right = TreeNode(arr[1])
    else:
        c = int(len(arr)/2)
        l_arr = arr[:c]
        r_arr = arr[c:]
        append_children_to_tree(root.left, l_arr, depth-1)
        append_children_to_tree(root.right, r_arr, depth-1)


def parse_tree(arr):
    arr = arr.copy()
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    r = 1
    d = 0
    len_of_children = 1
    while r < len(arr):
        d += 1
        len_of_children *= 2
        while r + len_of_children > len(arr):
            # Padding
            arr.append(None)
        append_children_to_tree(root, arr[r:(r+len_of_children)], d)
        r += len_of_children
    return root


def tree_to_arr(root):
    if root is None:
        return [None]
    ls = [root]
    rv = []
    while sum([1 if x is not None else 0 for x in ls]) > 0:
        rv += [x.val if x is not None else None for x in ls]
        nls_gen = ((x.left, x.right) if x is not None else (None, None) for x in ls)
        nls = []
        for l, r in nls_gen:
            nls += [l, r]
        ls = nls
    return rv
