class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return "Zamowienie: {}, {}, {}, {}".format(self.student, self.books, self.order_date, self.employee)
