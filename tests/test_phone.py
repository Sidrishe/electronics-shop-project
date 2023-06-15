from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture(autouse=True)
def cleanup_item():
    Item.all = []


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
