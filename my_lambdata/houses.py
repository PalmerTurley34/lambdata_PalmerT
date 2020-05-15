class House:
    def __init__(self, bedrooms, bathrooms, price):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price

    def info(self):
        print(f'This house has {self.bedrooms} bedrooms, {self.bathrooms} bathrooms, and is ${self.price}')


class Apartment(House):
    def __init__(self, bedrooms, bathrooms, price, apt_num):
        super().__init__(bedrooms, bathrooms, price)
        self.apt_num = apt_num

    def info(self):
        print(f'Apartment {self.apt_num} has {self.bedrooms} bedrooms, {self.bathrooms} bathrooms, and is ${self.price}')


if __name__ == '__main__':
    house1 = House(bedrooms='3', bathrooms='2', price='230,000')
    house1.info()

    apt1 = Apartment('2', '1.5', '185,000', '35')
    apt1.info()