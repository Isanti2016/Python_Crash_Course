"""
描述汽车电池和电动汽
车的模块
"""

class Battery():
    def __init__(self, battery_size=70):
        """初始化电池容量"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """描述电池容量信息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
    def get_range(self):
        """描述电池续航的消息"""
        if self.battery_size <= 70:
            range = 240
        if self.battery_size >70 and self.battery_size < 85:
            range = 250
        if self.battery_size >= 85:
            range = 270
        
        message = "This car can go approximaterly " + str(range)
        message += " miles on a full charge"
        print(message)

