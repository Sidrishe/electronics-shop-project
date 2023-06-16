"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest
import os

op_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src', "items.csv")


@pytest.fixture(autouse=True)
def cleanup_item():
    Item.all = []


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000


def test_all_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert Item.all == [item1, item2]


def test_item_name_setter():
    item = Item('test', 10.0, 5)
    item.name = 'newname'
    assert item.name == 'newname'

    with pytest.raises(ValueError):
        item.name = 'nameislongerthanten'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()

    item1 = Item.all[0]
    assert item1.name == "Смартфон"
    assert item1.price == 100
    assert item1.quantity == 1

    item2 = Item.all[1]
    assert item2.name == "Ноутбук"
    assert item2.price == 1000
    assert item2.quantity == 3


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
