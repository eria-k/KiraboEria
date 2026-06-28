class MobileMoney:
    def __init__(self):
        self.__balance = 1000
    def deposit(self, amount):
        self.__balance += amount   
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
eria = MobileMoney()
eria.deposit(500)
print(eria.get_balance())
eria.withdraw(200)
print(eria.get_balance())    
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
circ=Circle(5)
print(circ.area())        