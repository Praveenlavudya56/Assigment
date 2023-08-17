#--------class&object--------

# class Person:
#   def __init__(self, name, age,Roll):
#     self.name = name
#     self.age = age
#     self.Roll=Roll

# p1 = Person("praveen",24,9)

# print(p1.name)
# print(p1.age)
# print(p1.Roll)

#-----------Inharitence-----------------
#singil level inharitence
# class Perant:
#     def m1(self):
#         print('parent method')
# class Child(Perant):
#     def m2(self):
#         print('child method')
# obj=Child()
# obj.m1()
# obj.m2()
#---------------------------------------
#Multi-level inharitence
# class Perant:
#     def m1(self):
#         print('parent method')
# class Child(Perant):
#     def m2(self):
#         print('child method')
# class Subchild(Child):
#     def m3(self):
#         print('sub child method')
# c=Subchild()
# c.m1()
# c.m2()
# c.m3()
#----------------------------------------
#Hierarchical inharitence 
# class Perant:
#     def m1(self):
#         print('parent method')
# class Child1(Perant):
#     def m2(self):
#         print('child1 method')
# class Child2(Perant):
#     def m3(self):
#         print('child2 method')
# c1=Child1()
# c1.m1()
# c1.m2()
# c2=Child2()
# c2.m1()
# c2.m3()
#----------------------------------------
#Multiple inharitence

# class Perant1:
#     def m1(self):
#         print('perant1 method')
# class Perant2:
#     def m2(self):
#         print('perant2 method')
# class Child2(Perant1,Perant2):
#     def m3(self):
#         print('child2 method')
# c=Child2()
# c.m1()
# c.m2()
# c.m3()
# ---------------------------------------
#-------super class----------------------
# class A:
#     def __init__(self):
#         print('this is class A')
#     def fun1(self):
#         print('this is father class')
# class B(A):
#     def __init__(self):
#         print('this is class B')
#         super().__init__()
#         def fun2(self):
#             print('this is Mothar class')
# obj=B()
#------------------------------------------
#---------Polymorphism---------------------
# def add(a,b):
#     print(a+b)
# add(1,2)
# add('a','b')
# add([32,5],[7,4])
# add((6,7),(8,1))
#---------------------------
#1.method ovarloding
#method name is same deffrent parametears
# class Test:
#     def m1(self):
#         print('non-arg method')
#     def m1(self,a):
#         print('one-arg method')
#     def m1(self,a,b):
#         print('tow-arg method')
# t=Test()
# t.m1(10,20)
#--------------
# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=1):
#         return a+b+c
# obj=A()
# print(obj.sum(1,2,5))
#---------------------
#2.method over-riding
#same method name same parametar
# class A:
#     def display(self):
#         print('this is class A')
# class B(A):
#     def display(self):
#         print('this is class B')
#         super().display()
# obj=B()
# obj.display()
#-------------------------------
#---------Encapsulation---------
#public
#private__
#protected_

# class demo():
#     def __init__(self,a,b):
#      self.__a=a#privet
#      self._b=b#protected
# class demo2(demo):
#     def output(self):
#        print(self._b)
# d=demo2(3,4)
# d.output()
#-----------------------------
#--------Abstraction--------- 
# from abc import ABC, abstractmethod

# # Abstract class representing a Vehicle
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# # Concrete class representing a Car
# class Car(Vehicle):
#     def start(self):
#         print("Car started.")

#     def stop(self):
#         print("Car stopped.")

# # Concrete class representing a Bike
# class Bike(Vehicle):
#     def start(self):
#         print("Bike started.")

#     def stop(self):
#         print("Bike stopped.")

# # Function to use the Vehicle objects
# def drive_vehicle(vehicle):
#     vehicle.start()
#     vehicle.stop()

# # Create objects and use them
# car = Car()
# bike = Bike()

# drive_vehicle(car)
# drive_vehicle(bike)





   

            


   



        



