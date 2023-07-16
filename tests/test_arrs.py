from utils import arrs, dicts
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -4, "test") == "test"
    assert arrs.get([1, 2, 3], 3, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 5, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], 1, -2) == []
    assert arrs.my_slice([-1, -2, -3], 0) == [-1, -2, -3]
    assert arrs.my_slice([], ) == []
    assert arrs.my_slice([], 0, -1) == []
    assert arrs.my_slice([-6], -2) == [-6]


@pytest.fixture
def array():
    return {"vsc": "mercurial"}


def test_get_val(array):
    assert dicts.get_val(array, "vsc") == "mercurial"
    assert dicts.get_val(array, "vsc", "git") == "mercurial"
    assert dicts.get_val(array, "git") == "git"
    assert dicts.get_val(array, "git", "git") == "git"
    assert dicts.get_val(array, "git", "mercurial") == "mercurial"
    assert dicts.get_val({}, "vsc", "bazzar") == "bazzar"
