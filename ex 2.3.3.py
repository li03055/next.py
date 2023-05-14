class Octopus:
    count_animals = 0
    def __init__(self, name = 'Octavio'):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

def main():
    octopus1 = Octopus("lior")
    octopus2 = Octopus()
    print("octopus 1 name is: " + octopus1.get_name() + '\n' + "octopus 2 name is: " + octopus2.get_name())
    octopus1.set_name("agam")
    print("octopus 1 new name is: " + octopus1.get_name())
    print("number of octopuses: " + str(Octopus.count_animals))


if __name__ == '__main__':
    main()