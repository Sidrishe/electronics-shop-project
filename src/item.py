import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """Вернет название товара"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Проверяем длину названия товара"""
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError("Длина наименования товара не более 10 симвовов")
            # print("Длинна наименования товара не должна превышать 10 симвовов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализируюем экземпляр класса `Item` данными из файла _src/items.csv"""
        cls.all.clear()
        op_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src', "items.csv")
        with open(op_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row["name"], cls.string_to_number(row["price"]), int(row["quantity"])
                cls(name, price, quantity)
            #     name = row["name"]
            #     price = cls.string_to_number(row["price"])
            #     quantity = int(row["quantity"])

    @staticmethod
    def string_to_number(value):
        """Преобразование строки в число"""
        return int(float(value))
