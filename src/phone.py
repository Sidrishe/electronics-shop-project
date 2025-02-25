from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим карт
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает кол-вл сим карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
