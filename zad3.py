# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:19:58 2022

@author: Przemek
"""


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return "{} {} {} {} {}".format(self.area, self.rooms, self.price, self.address, self.plot)


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return "{} {} {} {} {}".format(self.area, self.rooms, self.price, self.address, self.floor)


domek1 = House("Katowice", 5, 800000, "Bogucice", 34)
mieszkanie1 = Flat("Katowice", 3, 500000, "Bogucice", 120)

print(domek1)
print(mieszkanie1)
