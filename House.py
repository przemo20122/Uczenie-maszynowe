import Property


class House(Property.Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return "{} {} {} {} {}".format(self.area, self.rooms, self.price, self.address, self.plot)
