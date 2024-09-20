class Coating():
    colors = ["Белый", "Синий", "Желтый", "Красный", "Перламутровый", "Серый металлик"]
    parts = ["Капот", "Передняя дверь", "Задняя дверь", "Передний бампер", "Задний бампер", "Крыша"]
    def __init__(self):
        self.part = None
        self.color = None
        self.price = None
        self.cost = 0
    def get_info(self):
        self.part = input(f"Введите название детали, Например {self.parts}: ")
        self.color = input(f"Введите цвет детали, Например: {self.colors}: ")
        
    def output_price(self):
        print(f"Цена покраски детали \"{self.part}\" в {self.color} составляет {self.price} рублей")
    def part_coefficient(self):
        color_coefficients = {
            "Белый": 1,
            "Синий": 1,
            "Желтый": 1.1,
            "Красный": 1,
            "Перламутровый": 1.2,
            "Серый металлик": 1.3
        }

        part_coefficients = {
            "Капот": 1,
            "Передняя дверь": 1.2,
            "Задняя дверь": 1.1,
            "Передний бампер": 1,
            "Задний бампер": 1,
            "Крыша": 1.1
        }

        base_price = 12000  


        color_coef = color_coefficients.get(self.color, 1)
        part_coef = part_coefficients.get(self.part, 1)


        self.price = base_price * color_coef * part_coef

if __name__ == '__main__':
    a1 = Coating()
    a1.get_info()
    a1.part_coefficient()
    a1.output_price()
