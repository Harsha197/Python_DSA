# class A:
#     def __init__(self,name,age,gender):
#         self.__name = name #private variable can be accessed inside of rhe same class which defines with __
#         self._age = age # protected variable can be accessed inside of the same class and its subclass which defines with _
#         self.gender = gender #public variable can be accessed inside of the same class and its subclass and outside of the class
# a1 = A("Yugesh",20,"Male")
# a2 = A("Picchi",23,"Male")
# print(a1._A__name)
# print(a1._age)
# print(a1.gender)
# print(a2._A__name)
# print(a2._age)
# print(a2.gender)

# class A:
#     def __init__(self,name,age,gender):
#         self.__name = name
#         self._age = age
#         self.gender = gender
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
# a1=A("Yugesh",20,"Male")
# a2=A("Picchi",23,"Male")
# a1.display()
# a2.display()

# from abc import ABC,abstractmethod
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance=amount
#     def getBalance(self):
#         return self.__balance
#     @abstractmethod
#     def intrestedcalc(self):
#         pass
# class SavingsAccount(BankAccount):
#     def intrestedcalc(self):
#         return self.getBalance()*0.05

#polymorphism:
# class Animal:
#     print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("woof")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")

