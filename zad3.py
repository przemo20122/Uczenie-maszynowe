# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:35:15 2022

@author: Przemek
"""
# zad 1
def function_print(name : str, surname : str):
    return f'Czesc {name} {surname}!'

wynik = function_print('Przemek', 'Bryja')
print(wynik)

# zad 2
def mnozenie(n : int,a : int):
    return n*a

print(mnozenie(2,5))

#zad 3
def jaka_liczba(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

wynik1 = jaka_liczba(6)
print('Liczba parzysta') if wynik1 else print('Liczba nieparzysta')

#zad 4
def suma_liczb(a : int,b : int,c : int) -> bool:
    if a+b >= c :
        return True
    else:
        return False

print(suma_liczb(4, 6, 2))

#zad 5
lista = [1,2,3,4,5,6]
def zad5(list1 : list,n : int) -> bool:
    return n in list1
    
print('Zawiera') if zad5(lista,8) else print('Nie zawiera')
# print(zad5(lista,8))

#zad 6
lista1 = [2,3,4] 
lista2 = [1,2]
def zad6(list1 : list,list2 : list) -> list:
    list3 = []
    list3 = list1+list2
    list3 = list(set(list3))
    return [n**3 for n in list3]

print(zad6(lista1,lista2))