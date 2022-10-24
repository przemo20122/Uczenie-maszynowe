import Property


class Flat(Property.Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return "{} {} {} {} {}".format(self.area, self.rooms, self.price, self.address, self.floor)
