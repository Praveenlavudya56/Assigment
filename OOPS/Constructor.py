# class Test:
#     def __init__(self):
#         print('Counstractar exeuction')
#     def m1(self):
#         print('Method exeuction')
# t1=Test()
# # t2=Test()
# # t3=Test()
# t1.m1()
#---------------------
class Student:
    '''
    This is student class with required data
    '''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print('Student Name:{}\nRollno:{}\nMarks:{}'.format(self.name,self.rollno,self.marks))

    s1=Student('praveen',101,80)
    s1.display()
    s2=Students('sunny',102,90)
    s2.display()
#------------------------------------------------

        