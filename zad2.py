# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:51:55 2022

@author: Przemek
"""
# zad 2a
n = ['Martin', 'Tom', 'Eva','Bob', 'Fin']
def print_names(names):
    for name in names:
        print(name)
print_names(n)

print('##########')
# zad 2b
liczby = [1,2,3,4,5]
def returns_num(numbers):
    for n in numbers:
        print(n*5)
    
returns_num(liczby)
print('##########') 
  
# zad 2c
n = (n for n in range(1,10))
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

even_numbers(n)
print('##########') 

# zad 2d
n = (n for n in range(1,10))
def second_numbers(numb):
    for i in range(1,10,2):
        print(i)

second_numbers(n)
