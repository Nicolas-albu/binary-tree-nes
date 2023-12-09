from binary_tree import BinaryTree


def test_whether_the_tree_is_complete_from_the_to_binary_tree_method():
    """Testa o método BinaryTree.to_binary_tree.

    Verifca se o método está criando corretamente uma árvore binária completa.
    """
    list_ = [4, 2, 6, 1, 3, 5, 7]
    tree = BinaryTree.to_binary_tree(list_)

    assert isinstance(tree, BinaryTree) and tree.value == 4
    assert isinstance(tree.left_tree, BinaryTree) and tree.left_tree.value == 2
    assert (
        isinstance(tree.right_tree, BinaryTree) and tree.right_tree.value == 6
    )
    assert (
        isinstance(tree.left_tree.left_tree, BinaryTree)
        and tree.left_tree.left_tree.value == 1
    )
    assert (
        isinstance(tree.left_tree.right_tree, BinaryTree)
        and tree.left_tree.right_tree.value == 3
    )
    assert (
        isinstance(tree.right_tree.left_tree, BinaryTree)
        and tree.right_tree.left_tree.value == 5
    )
    assert (
        isinstance(tree.right_tree.right_tree, BinaryTree)
        and tree.right_tree.right_tree.value == 7
    )


def test_whether_the_tree_is_incomplete_using_the_to_binary_tree_method():
    """Testa o método BinaryTree.to_binary_tree.

    Verifca se o método está criando corretamente uma árvore binária incompleta.
    """
    list_ = [10, 20, 3.6, 7.1, 8, 9]
    tree = BinaryTree.to_binary_tree(list_)

    assert isinstance(tree, BinaryTree) and tree.value == 10
    assert (
        isinstance(tree.left_tree, BinaryTree) and tree.left_tree.value == 20
    )
    assert (
        isinstance(tree.right_tree, BinaryTree)
        and tree.right_tree.value == 3.6
    )
    assert (
        isinstance(tree.left_tree.left_tree, BinaryTree)
        and tree.left_tree.left_tree.value == 7.1
    )
    assert (
        isinstance(tree.left_tree.right_tree, BinaryTree)
        and tree.left_tree.right_tree.value == 8
    )
    assert (
        isinstance(tree.right_tree.left_tree, BinaryTree)
        and tree.right_tree.left_tree.value == 9
    )


def test_whether_tree_complete_to_list_method():
    """Testa o método BinaryTree.to_list.

    Verifica se o método está retornando corretamente a árvore binária completa
    na forma de lista.
    """
    sub_tree1 = BinaryTree(
        0.875, left_tree=BinaryTree(20_112.334), right_tree=BinaryTree(111)
    )
    sub_tree2 = BinaryTree(
        19_202, left_tree=BinaryTree(0), right_tree=BinaryTree(1)
    )
    binary_tree = BinaryTree(0.1, left_tree=sub_tree1, right_tree=sub_tree2)

    assert binary_tree.to_list() == [0.1, 0.875, 19_202, 20_112.334, 111, 0, 1]


def test_whether_tree_incomplete_to_list_method():
    """Testa o método BinaryTree.to_list.

    Verifica se o método está retornando corretamente a árvore binária incompleta
    na forma de lista.
    """
    sub_tree1 = BinaryTree(9, left_tree=BinaryTree(7.3))
    sub_tree2 = BinaryTree(7)
    binary_tree = BinaryTree(0, left_tree=sub_tree1, right_tree=sub_tree2)

    assert binary_tree.to_list() == [0, 9, 7, 7.3]
