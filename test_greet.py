import pytest
from greet import greet


def test_greet_basic():
    assert greet("Claude") == "Hello, Claude!"


def test_greet_world():
    assert greet("world") == "Hello, world!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("")
