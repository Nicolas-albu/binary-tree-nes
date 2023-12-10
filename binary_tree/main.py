from __future__ import annotations

from typing import Sequence


class BinaryTree:
    """Classe responsável pela representação de uma (sub) árvore binária."""

    def __init__(
        self,
        /,
        value: float | int | None,
        *,
        left_tree: 'BinaryTree' | None = None,
        right_tree: 'BinaryTree' | None = None,
    ):
        """Inicializa uma (sub) árvore binária.

        Args:
            value (float): Valor do nó raiz da (sub) árvore.
            left_tree (BinaryTree, optional): Sub árvore binária à esquerda.
                O padrão é None.
            right_tree (BinaryTree, optional): Sub árvore binária à direita.
                O padrão é None.
        """
        self.__value = value
        self.__left_tree = left_tree
        self.__right_tree = right_tree

    @property
    def value(self) -> float | int | None:
        """Retorna a raiz da (sub) árvore binária."""
        return self.__value

    @value.setter
    def value(self, value: float | int | None):
        """Define o valor da raiz da (sub) árvore binária.

        Args:
            value (float | int | None): Valor da raiz da (sub) árvore binária.
        """
        if value is not None:
            self.__value = value

    @property
    def left_tree(self) -> 'BinaryTree' | None:
        """Retorna a sub árvore binária à esquerda."""
        return self.__left_tree

    @property
    def right_tree(self) -> 'BinaryTree' | None:
        """Retorna a sub árvore binária à direita."""
        return self.__right_tree

    @classmethod
    def to_binary_tree(
        cls, /, list_: Sequence[int | float], *, node_index: int | None = 0
    ) -> 'BinaryTree':
        """Cria uma (sub) árvore binária.

        Args:
            list_ (Sequence[float]): Lista de valores a serem transformados em árvore
                binária.
            node_index (int, optional): Sub árvore binária à esquerda.
                O padrão é 0.

        Returns:
            BinaryTree: uma (sub) árvore binária.
        """
        if node_index is None:
            return cls(None)

        actual_value = list_[node_index]
        left_node, right_node = 2 * node_index + 1, 2 * node_index + 2

        if left_node >= len(list_):
            left_node = None

        if right_node >= len(list_):
            right_node = None

        return cls(
            actual_value,
            left_tree=cls.to_binary_tree(list_, node_index=left_node),
            right_tree=cls.to_binary_tree(list_, node_index=right_node),
        )

    @staticmethod
    def _to_list(tree: 'BinaryTree', tree_list: list[int | float]):
        """Função auxiliar para percorrer a árvore e adicionar valores à lista.

        Args:
            tree (BinaryTree): (Sub) árvore binária.
            tree_list (list[int | float]): Lista de valores da árvore binária.
        """
        if tree.left_tree and tree.left_tree.value is not None:
            tree_list.append(tree.left_tree.value)

        if tree.right_tree and tree.right_tree.value is not None:
            tree_list.append(tree.right_tree.value)

        for child_node in (tree.left_tree, tree.right_tree):
            if child_node:
                BinaryTree._to_list(child_node, tree_list)

    def to_list(self) -> list[int | float]:
        """Converte a árvore binária atual em uma lista.

        Returns:
            list[int | float]: Lista com os valores da árvore binária atual.
        """
        if self.__value is None:
            return []

        binary_tree_list = [self.__value]
        self._to_list(self, binary_tree_list)

        return binary_tree_list

    def heapify(self):
        """Converte a árvore binária atual em um Árvore Heap Min-Max."""
        largest, actual_node = self.__value, self
        left_node, right_node = self.__left_tree, self.__right_tree

        if left_node and left_node.value is not None and left_node > largest:
            largest, actual_node = left_node.value, left_node

        if (
            right_node
            and right_node.value is not None
            and right_node > largest
        ):
            largest, actual_node = right_node.value, right_node

        if largest != self.__value:
            self.__value, actual_node.value = largest, self.__value

            actual_node.heapify()

    def __eq__(self, other):
        """Verifica se as (sub) árvore binárias são iguais."""
        if not isinstance(other, BinaryTree):
            return False

        return self.to_list() == other.to_list()

    def __gt__(self, other):
        """Verifica se o primeiro valor da (sub) árvore binária é maior."""
        if (
            isinstance(other, BinaryTree)
            and self.__value is not None
            and other.value is not None
        ):
            return self.__value > other.value

        if (
            isinstance(other, int) or isinstance(other, float)
        ) and self.__value is not None:
            return self.__value > other

    def __repr__(self):
        """Retorna uma representação em string da (sub) árvore binária."""
        if self.value is None:
            return 'BinaryTree(None)'

        return (
            f'BinaryTree({self.value}, left_tree={self.left_tree},'
            f' right_tree={self.right_tree})'
        )
