import pytest
import homework

def test_first():
    assert homework.first_func() == ["Hi", 5, 3.14, True]


def test_second():
    assert homework.second_func(1) == 1
    assert homework.second_func(4) == 0
    assert homework.second_func(8) == 0
    assert homework.second_func(9) == 2


def test_third():
    assert homework.third_func(1, 9) == 10
    assert homework.third_func("Hello ", "World") == "Hello World"
    assert homework.third_func(5, "hi") == "Failed"


def test_fourth():
    assert homework.fourth_func(3) == "HiHiHi"
    assert homework.fourth_func(1) == "Hi"
    assert homework.fourth_func(4) == "HiHiHiHi"


def test_fifth():
    assert homework.fifth_func(1,1,1) == 1
    assert homework.fifth_func(1,2,3) == 6
    assert homework.fifth_func(2,2,2.5) == 10