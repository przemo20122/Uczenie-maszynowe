# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:33:18 2022

@author: Przemek
"""

# lab 3
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @property
    def name(self):
        return self.name
    def marks(self):
        return self.marks
    
    @name.setter
    def name(self, name: str):
        self._name = name    
        
    def marks(self, value: int):
        self._marks = value
    
    def is_passed(self) -> bool:
        if(self.marks > 50):
            return True
        else:
            return False

student1 = Student("Przemek", 56)
student2 = Student("Monika", 42)

print(student1.is_passed())
print(student2.is_passed())
        