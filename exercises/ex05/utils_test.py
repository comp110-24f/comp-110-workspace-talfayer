"""EX05 tests"""

__author__ = "730646268"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index

#tests for only_evens
def test_only_evens_return() -> None:
    """test that the function returns the correct value"""
    list1: list[int] = [1, 2, 3, 4]
    assert(only_evens(list1)) == [2, 4]

def test_only_evens_mutates() -> None:
    """test that the function works correctly"""
    list1: list[int] = [1, 2, 3, 4]
    list_evens: list[int] = [2, 4]
    assert(only_evens(list1)) == list_evens

def test_only_evens_edge() -> None:
    """test only_evens with an empty list"""
    list1: list[int] = []
    assert(only_evens(list1)) == []

#tests for sub
def test_sub_return() -> None:
    """test that sub returns the right value"""
    list1: list[int] = [1, 2, 3, 4]
    assert(sub(list1, 1, 3)) == [2, 3]

def test_sub_mutates() -> None:
    """test that the function works correctly"""
    list1: list[int] = [1, 2, 3, 4]
    list_mutated: list[int] = [2,3]
    assert(sub(list1, 1, 3)) == list_mutated 

def test_sub_edge() -> None:
    """tests the function with an edge case - range is out of bounds"""
    list1: list[int] = [1, 2, 3, 4]
    assert(sub(list1, -1, 3)) == [1, 2, 3]

#tests for add_at_index
import pytest

def test_add_at_index_raises_indexerror():
    """Test that ass_at_index raises an IndexError for an individual index."""
    # your object to pass to add_at_index
    with pytest.raises(IndexError):
        add_at_index(<list_object>, <value_to_add>, <index_to_insert_num>)
    #an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num> that is greater than the length of our <list_object>

def test_add_at_index_return() -> None:
    """test that adding the number returns the right value"""
    list1: list[int] = [1, 2, 4]
    assert(add_at_index(list1, 3, 2)) == [1, 2, 3, 4]

def test_add_at_index_mutates() -> None:
    """test that the function works properly"""
    list1: list[int] = [1, 2, 4]
    list_added: list[int] = [1, 2, 3, 4]
    assert(add_at_index(list1, 3, 2)) == list_added

