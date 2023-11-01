"""
    pytest tests
"""
# test_my_module.py

from my_module import add


def test_add():
    """
    unit test for addition
    """
    assert add(1, 2) == 3
    assert add(5, 7) == 12
    assert add(0, 0) == 0
