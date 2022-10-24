# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:57:12 2022

@author: Przemek
"""
import Order
import Student
import Book
import Employee
import Library

library1 = Library.Library("Katowice", "Kosciuszki", "44-040", "9-19", "321312421412")
library2 = Library.Library("Krakow", "Nowa", "30-000", "9-20", "21472470821")

employee1 = Employee.Employee("Michal", "Nowak", "01-01-2020", "04-02-1990", "Katowice", "Poniatowskiego", "44-040",
                              "12345667889")
employee2 = Employee.Employee("Jan", "Kowal", "01-01-2021", "12-05-1995", "Katowice", "3 maja", "44-040", "12345667889")
employee3 = Employee.Employee("Przemek", "Bochenek", "01-01-2008", "23-09-1980", "Katowice", "Adamskiego", "44-040",
                              "12345667889")

book1 = Book.Book(library1, "20-02-2009", "Remigiusz", "Mroz", "340")
book2 = Book.Book(library1, "20-04-2012", "Remigiusz", "Mroz", "420")
book3 = Book.Book(library1, "25-03-2016", "Remigiusz", "Mroz", "300")
book4 = Book.Book(library1, "20-06-2010", "Remigiusz", "Mroz", "290")
book5 = Book.Book(library1, "20-07-2018", "Remigiusz", "Mroz", "380")

order1 = Order.Order(employee1, "Ktos", book1, "20-10-2022")
# order2 = Order(employee, student, books, order_date)
print(order1)

# print(library1)
# print(employee1)
# print(book1)
