"""
描述电动汽车的模块
"""
from car import Car
from battery import Battery

class ElectricCar(Car):
    """模拟电动汽车的类"""
    def __init__(self, make, model, year):
        """初始化电动汽车"""
        super().__init__(make, model, year)
        self.battery = Battery()

