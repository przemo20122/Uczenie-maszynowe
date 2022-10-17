# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:57:12 2022

@author: Przemek
"""

class Library():
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        
    def __str__(self):
        return "Biblioteka: {}, {}, {}, {}, {}".format(self.city, self.street, self.zip_code, self.open_hours, self.phone) 
        
class Employee():
    def __init__(self, first_name, last_name,hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        
    def __str__(self):
        return "Prac:{}, {}, {}, {}, {}, {}, {}, {}".format(self.first_name, self.last_name, self.hire_date, self.birth_date, self.city, self.street, self.zip_code, self.phone) 

        
class Book():
    def __init__(self, librabry, publication_date, author_name, author_surname, number_of_pages):
        self.librabry = librabry
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        
    def __str__(self):
        return "Ksiazka:{}, {}, {}, {}, {}".format(self.librabry, self.publication_date, self.author_name, self.author_surname, self.number_of_pages)

class Student():
    def __init__(self, name):
        self.name = name
        
class Order():
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    
    def __str__(self):
        return "Zamowienie: {}, {}, {}, {}".format(self.student, self.books, self.order_date, self.employee)

library1 = Library("Katowice", "Kosciuszki", "44-040", "9-19", "321312421412")
library2 = Library("Krakow", "Nowa", "30-000", "9-20", "21472470821")

employee1 = Employee("Michal", "Nowak", "01-01-2020", "04-02-1990", "Katowice", "Poniatowskiego", "44-040", "12345667889")
employee2 = Employee("Jan", "Kowal", "01-01-2021", "12-05-1995", "Katowice", "3 maja", "44-040", "12345667889")
employee3 = Employee("Przemek", "Bochenek", "01-01-2008", "23-09-1980", "Katowice", "Adamskiego", "44-040", "12345667889")

book1 = Book(library1, "20-02-2009", "Remigiusz", "Mroz", "340")
book2 = Book(library1, "20-04-2012", "Remigiusz", "Mroz", "420")
book3 = Book(library1, "25-03-2016", "Remigiusz", "Mroz", "300")
book4 = Book(library1, "20-06-2010", "Remigiusz", "Mroz", "290")
book5 = Book(library1, "20-07-2018", "Remigiusz", "Mroz", "380")

order1 = Order(employee1, "Ktos", book1, "20-10-2022")
# order2 = Order(employee, student, books, order_date)
print(order1)

# print(library1)
# print(employee1)
# print(book1)