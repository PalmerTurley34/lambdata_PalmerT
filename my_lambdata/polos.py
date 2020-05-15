
class Polo:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def wash(self):
        print(f'Washing the {self.size} {self.color} polo')

if __name__ == "__main__":


    polo = Polo(size='Large', color='Blue')
    print(polo.size, polo.color)
    polo.wash()

    polo2 = Polo(size='Small', color='Yellow')
    print(polo2.size, polo2.color)
    polo2.wash()