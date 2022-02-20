from models.algorithm.algorithm import SplayTree
import pytest

from utilities.sort_utility import is_sorted


@pytest.mark.parametrize("data, expected_state",
                         [
                             ([5, 4, 6 , 6, 1, 1, 10, 3, 4, 0, 11],
                              [
                                  [5],
                                  [4, 5],
                                  [4, 5, 6],
                                  [4, 5, 6, 6],
                                  [1, 4, 5, 6, 6],
                                  [1, 1, 4, 5, 6, 6],
                                  [1, 1, 4, 5, 6, 6, 10],
                                  [1, 1, 3, 4, 5, 6, 6, 10],
                                  [1, 1, 3, 4, 4, 5, 6, 6, 10],
                                  [0, 1, 1, 3, 4, 4, 5, 6, 6, 10],
                                  [0, 1, 1, 3, 4, 4, 5, 6, 6, 10, 11],
                                  [0, 1, 1, 3, 4, 4, 5, 6, 6, 10, 10, 11],
                              ])

                         ])
def test_inner_state_tree(data, expected_state):
    """
       Проверка того, что при обходе дерева Left Node -> Root -> Right node
       получаем отсортированный список
    """
    spltree = SplayTree()
    for i, val in enumerate(data):
        spltree.insert(val)
        assert spltree.inorder() == expected_state[i], f'На шаге {i} неверное состояние'

@pytest.mark.parametrize("data, expected_state",
                         [
                             ([5, 4, 6, 6, 1, 1, 10, 3, 4, 0, 11],
                              [
                                  [1, True],
                                  [2, False],
                                  [11, True],
                                  [-1, False]
                              ])

                         ])
def test_search_tree(data, expected_state):
    """
       Проверка того, что при поиске элемента находится Node, если есть в дереве
    """
    spltree = SplayTree()
    for val in data:
        spltree.insert(val)

    for key, exp_found in expected_state:
        node = spltree.search_tree(key)
        not_none = node != None
        assert not_none == exp_found, f'Поиск элемента {key} выдал не тот результат'
        if not_none:
            assert key == node.data, f'Node с ключем {key} имеет другое значение'

