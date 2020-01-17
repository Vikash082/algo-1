###############################################################################
#                                                                             #
#                          invert binary tree                                 #
#                                                                             #
###############################################################################

# Below solution is recursive one. Iterative sol is equally good.


# T: O(n), S: O(depth of tree)
def invert_tree_recursively(tree):
    if not tree:
        return
    else:
        swap_nodes_child(tree)
        invert_tree_recursively(tree.left)
        invert_tree_recursively(tree.right)


def swap_nodes_child(node):
    tmp = node.left
    node.left = node.right
    node.right = tmp
