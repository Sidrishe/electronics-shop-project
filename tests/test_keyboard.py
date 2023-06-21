import pytest
from src.keyboard import Keyboard


def test_init_():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)

    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == "EN"


def test_change_language():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)

    assert keyboard.language == "EN"

    keyboard.change_lang()
    assert keyboard.language == "RU"

    keyboard.change_lang()
    assert keyboard.language == "EN"


def test_str():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)

    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"


def test_setter():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)

    assert keyboard.language == "EN"

    keyboard.language = "RU"
    assert keyboard.language == "RU"

    with pytest.raises(AttributeError):
        keyboard.language = "CH"
