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
        '''
        TODO: Записать финальную цену в self.price
        '''
        pass

if __name__ == '__main__':
    a1 = Coating()
    a1.get_info()
    a1.output_price()
