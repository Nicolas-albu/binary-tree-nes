from __future__ import annotations


class BinaryTree:
    """Classe responsável pela representação de uma (sub) árvore binária."""

    def __init__(
        self,
        /,
        value: float | None,
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
    def root(self):
        """Retorna a raiz da (sub) árvore binária."""
        return self.__value

    @property
    def left_tree(self):
        """Retorna a sub árvore binária à esquerda."""
        return self.__left_tree

    @property
    def right_tree(self):
        """Retorna a sub árvore binária à direita."""
        return self.__right_tree

    @classmethod
    def to_binary_tree(
        cls, /, list_: list[int] | list[float], *, node_index: int | None = 0
    ) -> 'BinaryTree':
        """Cria uma (sub) árvore binária.

        Args:
            list_ (list[float]): Lista de valores a serem transformados em árvore
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

    def __repr__(self):
        """Retorna uma representação em string da (sub) árvore binária."""
        if self.root is None:
            return 'BinaryTree(None)'

        return (
            f'BinaryTree({self.root}, left_tree={self.left_tree},'
            f' right_tree={self.right_tree})'
        )
