from models.algorithm.algorithm import heap_sort
import pytest

from utilities.sort_utility import is_sorted


class TestHeapSort:

    def test_heap_sort(self, random_array):
        heap_sort(random_array)
        assert is_sorted(random_array), "array is not sorted"

    @pytest.mark.parametrize("test_arr, expected_arr",
                             [([], []),
                              ([1], [1]),
                              ([1, 2, 3], [1, 2, 3]),
                              ([1, 2, 1], [1, 1, 2])
                              ])
    def test_heap_sort_par(self, test_arr, expected_arr):
        heap_sort(test_arr)
        assert test_arr == expected_arr, "array is not sorted"
