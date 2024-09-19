class Coating():
    def __init__(self):
        self.part = None
        self.color = None
        self.cost = 0
    def get_info(self):
        self.part = input(f"Введите название детали, Например {self.parts}: ")
        self.color = input("Введите цвет детали, Например: {self.colors}: ")
        
    def output_price(self):
        pass
    def part_coefficient(self):
        pass

if __name__ == '__main__':
    pass


