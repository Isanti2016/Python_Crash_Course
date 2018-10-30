"""描述汽车的基类"""

class Car():
    """尝试模拟汽车"""
    def __init__(self, make, model, year):
        """car初始化函数"""
        self.make  = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_description_name(self):
        """整洁的描述性名称"""
        long_name = str(self.year) + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条消息，指出汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it!")
        
    def update_odometer(self, mileage):
        """
        设置指定的里程数
        拒绝将里程数回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """将里程数增加指定的量"""
        self.odometer_reading += miles
        
