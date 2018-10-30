
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title() + " is now sitting!")
    
    def roll_over(self):
        """模拟小狗大滚"""
        print(self.name.title + "is now rolled over!")
        
my_dog = Dog("feigei", 6)

my_dog.sit()

print("my dog is " + str(my_dog.age) + " years old")
