"""
主函数
"""

from car import Car
from electric_car import ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2018)

print(my_tesla.get_description_name() )
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.update_odometer(90)
my_tesla.read_odometer()
