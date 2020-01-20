###############################################################################
#                                                                             #
#                     Depth First Search                                      #
#                                                                             #
###############################################################################


# T: O(V+E)  S: O(V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))

    def depth_first_traversal(self, array):
        # add the node
        array.append(self.name)
        for children in self.children:
            # call dfs on its child
            children.depth_first_traversal(array)
        return array
