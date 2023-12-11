import ipdb
import pytest

from binary_tree import BinaryTree


@pytest.fixture
def strictly_binary_tree():
    """Retorna uma árvore estritamente binária.

    Uma árvore estritamente binária é um tipo de árvore binária em que cada nó
    tem 0 ou 2 filhos. Em outras palavras, cada nó é ou uma folha ou tem dois
    filhos.
    """
    # [0.1, -1, 8.35, -2, 0.5]
    yield BinaryTree(
        0.1,
        left_tree=BinaryTree(
            -1, left_tree=BinaryTree(-2), right_tree=BinaryTree(0.5)
        ),
        right_tree=BinaryTree(8.35),
    )


@pytest.fixture
def complete_binary_tree():
    """Retorna uma árvore estritamente binária.

    Uma árvore binária em que todos os níveis, exceto possivelmente o último,
    estão completamente preenchidos, e todos os nós são o mais à esquerda
    possível.
    """
    # [-1, -2.3, -22_122e-20, 0, 0, -1.3, 7, -8]
    yield BinaryTree(
        -1,
        left_tree=BinaryTree(
            -2.3,
            left_tree=BinaryTree(0, left_tree=BinaryTree(-8)),
            right_tree=BinaryTree(0),
        ),
        right_tree=BinaryTree(
            -22_122e-20, left_tree=BinaryTree(-1.3), right_tree=BinaryTree(7)
        ),
    )


@pytest.fixture
def perfect_binary_tree():
    """Retorna uma árvore perfeita.

    Uma árvore perfeita é uma árvore binária em que todos os níveis
    estão completamente preenchidos.
    """
    # [0, 0.667, 19_202, 22_332e1, 1, 1, 1]
    yield BinaryTree(
        0,
        left_tree=BinaryTree(
            0.667, left_tree=BinaryTree(22_332e1), right_tree=BinaryTree(1)
        ),
        right_tree=BinaryTree(
            19_202, left_tree=BinaryTree(1), right_tree=BinaryTree(1)
        ),
    )


def test_strictly_binary_tree_to_binary_tree_method():
    """Testa o método BinaryTree.to_binary_tree.

    Verifca se o método está criando corretamente uma árvore estritamente binária.
    """
    list_tree = [0.1, -1, 8.35, -2, 0.5]
    tree = BinaryTree.to_binary_tree(list_tree)

    assert isinstance(tree, BinaryTree)
    assert isinstance(tree.left_tree, BinaryTree)
    assert isinstance(tree.right_tree, BinaryTree)
    assert isinstance(tree.left_tree.left_tree, BinaryTree)
    assert isinstance(tree.left_tree.right_tree, BinaryTree)

    assert tree.value == 0.1
    assert tree.left_tree.value == -1
    assert tree.right_tree.value == 8.35
    assert tree.left_tree.left_tree.value == -2
    assert tree.left_tree.right_tree.value == 0.5


def test_complete_binary_tree_to_binary_tree_method():
    """Testa o método BinaryTree.to_binary_tree.

    Verifca se o método está criando corretamente uma árvore binária completa.
    """
    list_tree = [-1, -2.3, -22_122e-20, 0, 0, -1.3, 7, -8]
    tree = BinaryTree.to_binary_tree(list_tree)

    assert isinstance(tree, BinaryTree)
    assert isinstance(tree.left_tree, BinaryTree)
    assert isinstance(tree.right_tree, BinaryTree)
    assert isinstance(tree.left_tree.left_tree, BinaryTree)
    assert isinstance(tree.left_tree.right_tree, BinaryTree)
    assert isinstance(tree.right_tree.left_tree, BinaryTree)
    assert isinstance(tree.right_tree.right_tree, BinaryTree)
    assert isinstance(tree.left_tree.left_tree.left_tree, BinaryTree)

    assert tree.value == -1
    assert tree.left_tree.value == -2.3
    assert tree.right_tree.value == -22_122e-20
    assert tree.left_tree.left_tree.value == 0
    assert tree.left_tree.right_tree.value == 0
    assert tree.right_tree.left_tree.value == -1.3
    assert tree.right_tree.right_tree.value == 7
    assert tree.left_tree.left_tree.left_tree.value == -8


def test_perfect_binary_tree_to_binary_tree_method():
    """Testa o método BinaryTree.to_binary_tree.

    Verifca se o método está criando corretamente uma árvore binária perfeita.
    """
    list_tree = [0, 0.667, 19_202, 22_332e1, 1, 1, 1]
    tree = BinaryTree.to_binary_tree(list_tree)

    assert isinstance(tree, BinaryTree)
    assert isinstance(tree.left_tree, BinaryTree)
    assert isinstance(tree.right_tree, BinaryTree)
    assert isinstance(tree.left_tree.left_tree, BinaryTree)
    assert isinstance(tree.left_tree.right_tree, BinaryTree)
    assert isinstance(tree.right_tree.left_tree, BinaryTree)
    assert isinstance(tree.right_tree.right_tree, BinaryTree)

    assert tree.value == 0
    assert tree.left_tree.value == 0.667
    assert tree.right_tree.value == 19_202
    assert tree.left_tree.left_tree.value == 22_332e1
    assert tree.left_tree.right_tree.value == 1
    assert tree.right_tree.left_tree.value == 1
    assert tree.right_tree.right_tree.value == 1


def test_strictly_binary_tree_to_list_method(strictly_binary_tree):
    """Testa o método BinaryTree.to_list.

    Verifica se o método está retornando corretamente a árvore estritamente binária
    na forma de lista.
    """
    assert strictly_binary_tree.to_list() == [0.1, -1, 8.35, -2, 0.5]


def test_complete_binary_tree_to_list_method(complete_binary_tree):
    """Testa o método BinaryTree.to_list.

    Verifica se o método está retornando corretamente a árvore binária completa
    na forma de lista.
    """
    assert complete_binary_tree.to_list() == [
        -1,
        -2.3,
        -22_122e-20,
        0,
        0,
        -1.3,
        7,
        -8,
    ]


def test_perfect_binary_tree_to_list_method(perfect_binary_tree):
    """Testa o método BinaryTree.to_list.

    Verifica se o método está retornando corretamente a árvore binária perfeita
    na forma de lista.
    """
    assert perfect_binary_tree.to_list() == [
        0,
        0.667,
        19_202,
        22_332e1,
        1,
        1,
        1,
    ]


def test_strictly_binary_tree_heapify_method(strictly_binary_tree):
    """Testa o método BinaryTree.heapify.

    Verifica se o método está retornando corretamente o Heap da árvore
    estritamente binária.
    """
    # [0.1, -1, 8.35, -2, 0.5]
    strictly_binary_tree = strictly_binary_tree.heapify()

    # [-2, -1, 8.35, 0.1, 0.5]
    heap_tree = BinaryTree(
        -2,
        left_tree=BinaryTree(
            -1, left_tree=BinaryTree(0.1), right_tree=BinaryTree(0.5)
        ),
        right_tree=BinaryTree(8.35),
    )

    assert strictly_binary_tree == heap_tree


def test_complete_binary_tree_heapify_method(complete_binary_tree):
    """Testa o método BinaryTree.heapify.

    Verifica se o método está retornando corretamente o Heap da árvore
    binária completa.
    """
    # [-1, -2.3, -22_122e-20, 0, 0, -1.3, 7, -8]
    complete_binary_tree = complete_binary_tree.heapify()

    # [-8, -2.3, -1.3, -1, 0, -22_122e-20, 7, 0]
    heap_tree = BinaryTree(
        -8,
        left_tree=BinaryTree(
            -2.3,
            left_tree=BinaryTree(-1, left_tree=BinaryTree(0)),
            right_tree=BinaryTree(0),
        ),
        right_tree=BinaryTree(
            -1.3, left_tree=BinaryTree(-22_122e-20), right_tree=BinaryTree(7)
        ),
    )

    assert complete_binary_tree == heap_tree


def test_perfect_binary_tree_heapify_method(perfect_binary_tree):
    """Testa o método BinaryTree.heapify.

    Verifica se o método está retornando corretamente o Heap da árvore
    binária perfeita.
    """
    # [0, 0.667, 19_202, 22_332e1, 1, 1, 1]
    perfect_binary_tree = perfect_binary_tree.heapify()

    # [0, 0.667, 1, 22_332e1, 1, 1, 19_202]
    heap_tree = BinaryTree(
        0,
        left_tree=BinaryTree(
            0.667, left_tree=BinaryTree(22_332e1), right_tree=BinaryTree(1)
        ),
        right_tree=BinaryTree(
            1, left_tree=BinaryTree(1), right_tree=BinaryTree(19_202)
        ),
    )

    assert perfect_binary_tree == heap_tree
