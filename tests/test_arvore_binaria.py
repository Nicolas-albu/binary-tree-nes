import pytest

from binary_tree import BinaryTree


@pytest.fixture
def binary_tree_any() -> BinaryTree:
    """Retorna uma instância da classe BinaryTree."""
    return BinaryTree(4, left_tree=BinaryTree(2), right_tree=BinaryTree(6))


def test_whether_the_tree_is_complete_from_the_to_binary_tree_method():
    """Testa a criação de uma instância da classe BinaryTree."""
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
