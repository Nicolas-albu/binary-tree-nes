from setuptools import setup

packages = ['binary_tree']

package_data = {'': ['*']}

setup_kwargs = {
    'name': 'binary-tree-nes',
    'version': '0.1.0',
    'description': 'Implementação da estrutura de árvore binária.',
    'long_description': open('README.md', encoding='utf-8').read(),
    'author': 'Nícolas Albuquerque Ramos',
    'author_email': 'nicolas.albu@outlook.com',
    'url': 'https://github.com/Nicolas-albu/binary-tree-nes/tree/main',
    'packages': packages,
    'python_requires': '==3.10.*',
}

setup(**setup_kwargs)
