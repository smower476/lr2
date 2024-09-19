class Coating():
    colors = ["Белый", "Синий", "Желтый", "Красный", "Перламутровый", "Серый металлик"]
    parts = ["Капот", "Передняя дверь", "Задняя дверь", "Передний бампер", "Задний бампер", "Крыша"]
    def __init__(self):
        self.part = None
        self.color = None
        self.price = None
        self.cost = 0
    def get_info(self):
        pass
    def output_price(self):
        print(f"Цена покраски детали \"{self.part}\" в {self.color} составляет {self.price} рублей")
    def part_coefficient(self):
        pass

if __name__ == '__main__':
    a1 = Coating()
    a2 = Coating()
    pass