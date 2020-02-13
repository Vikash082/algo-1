class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


def validate_bst(tree):
    return validate_bst_helper(float("-inf"), tree, float("inf"))


def validate_bst_helper(min_val, tree, max_val):
    if not tree:
        return True

    if min_val > tree.value or tree.value >= max_val:
        return False

    valid_left = validate_bst_helper(min_val, tree.left, tree.value)
    return valid_left and validate_bst_helper(
            tree.value, tree.right, max_val)


if __name__ == '__main__':
    tree1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(
        22).insert(13).insert(14)
    print(validate_bst(tree1))

    tree2 = (
        BST(10)
        .insert(5)
        .insert(15)
        .insert(5)
        .insert(2)
        .insert(1)
        .insert(22)
        .insert(-5)
        .insert(-15)
        .insert(-5)
        .insert(-2)
        .insert(-1)
        .insert(-22)
    )
    print(validate_bst(tree2))

    tree3 = (
        BST(10)
        .insert(5)
        .insert(15)
        .insert(5)
        .insert(2)
        .insert(1)
        .insert(22)
        .insert(-5)
        .insert(-15)
        .insert(-5)
        .insert(-2)
        .insert(-1)
        .insert(-22)
        )
    tree3.left.left.left.left.left.left.left = BST(11)
    print(validate_bst(tree3))
