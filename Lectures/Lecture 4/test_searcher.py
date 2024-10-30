import pytest
import searcher


def test_linear_search():
    arr = list(range(5))
    assert searcher.linear_search(arr, 5) == -1
    assert searcher.linear_search(arr, 3) == 3


def test_incorrectly():
    print("run")
    arr = []
    assert searcher.linear_search(arr, 5) == 1