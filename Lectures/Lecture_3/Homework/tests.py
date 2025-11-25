import pytest
import homework

def assert_lists_equal(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    for idx in len(a):
        if a[idx] != b[idx]:
            return False
    return True


def test_list_one():
    actual = homework.list_one()
    expected = [1,3,5,7,9]
    assert_lists_equal(actual, expected)


def test_list_two():
    actual = homework.list_two([1,2,3,4,5,6,3,4,2])
    expected = [2, 4, 6, 4, 2]
    assert_lists_equal(actual, expected)
    actual = homework.list_two([])
    expected = []
    assert_lists_equal(actual, expected)
    actual = homework.list_two([143, 294, 2919487])
    expected = [294]
    assert_lists_equal(actual, expected)


def test_list_three():
    sorted_list = [1,3,4,6,10,15,204,698,1024]
    actual = homework.list_three(sorted_list, 4)
    expected = 2
    assert actual == expected
    actual = homework.list_three(sorted_list, 25)
    expected = -1
    assert actual == expected
    actual = homework.list_three(sorted_list, 698)
    expected = 7
    assert actual == expected


def assert_dicts_equal(a: dict, b: dict) -> bool:
    if len(a.keys()) != len(b.keys()):
        return False
    for k in a.keys():
        if k not in b.keys():
            return False
        if b[k] != a[k]:
            return False
    return True

def test_dict_one():
    actual = homework.dict_one()
    expected = {"dog": "bark", "cat": "meow", "duck": "quack"}
    assert_dicts_equal(actual, expected)


def test_dict_two():
    base_dict = {"dog": "bark", "cat": "meow", "duck": "quack"}
    actual = homework.dict_two(base_dict, key="dog", value="bark")
    assert actual
    actual = homework.dict_two(base_dict, key="owl", value="hoot")
    assert not actual
    base_dict["owl"] = "hoot"
    actual = homework.dict_two(base_dict, key="owl", value="hoot")
    assert actual
    actual = homework.dict_two(base_dict, key="owl", value="caw")
    assert not actual
    

def test_bonus():
    base_arr = [3, 1, 7, 2, 11]
    res = homework.bonus(base_arr, 7)
    assert not res
    res = homework.bonus(base_arr, 13)
    assert res
    res = homework.bonus(base_arr, 3)
    assert res