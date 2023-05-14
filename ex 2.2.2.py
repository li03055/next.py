class Octopus:
    def __init__(self, age):
        self.name = 'Octavio'
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

def main():
    octopus1 = Octopus(7)
    octopus2 = Octopus(5)
    octopus1.birthday()
    print("octopus 1 age is: " + str(octopus1.get_age()) + '\n' + "octopus 2 age is: " + str(octopus2.get_age()))

if __name__ == '__main__':
    main()