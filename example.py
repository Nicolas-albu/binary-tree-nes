from binary_tree import BinaryTree

# Construa uma árvore binária manualmente
tree1 = BinaryTree(1, left_tree=BinaryTree(2), right_tree=BinaryTree(3))

# Construa uma árvore binária a partir de uma lista
values = [0, 0.667, 19_202, 22_332e1, 1, 1, 1]
tree2 = BinaryTree.to_binary_tree(values)

# Transforme uma árvore binária BinaryTree em uma lista
tree1.to_list()
# [1, 2, 3]

# Transforme uma árvore binária BinaryTree em um Min-Max Heap
tree2 = tree2.heapify()
# [0, 0.667, 1, 22_332e1, 1, 1, 19_202]

# Imprima a árvore binária
print(tree2)
# ou
print(tree2.print_tree())
# "Depois do tree2.heapify() acima ela está heapificada."
#
# ROOT: 0
#     LEFT--> 0.667
#         LEFT--> 223320.0
#         RIGHT--> 1
#     RIGHT--> 1
#         LEFT--> 1
#         RIGHT--> 19202
