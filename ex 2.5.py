class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger = 0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass




class Dog(Animal):
    def __init__(self, name, hunger = 0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")



class Cat(Animal):
    def __init__(self, name, hunger = 0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")



class Skunk(Animal):
    def __init__(self, name, hunger = 0, stink_count = 6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")



class Unicorn(Animal):
    def __init__(self, name, hunger = 0):
        super().__init__(name, hunger)

    def talk(self):
        print("good day, darling")

    def sing(self):
        print("I’m not your toy...")



class Dragon(Animal):
    def __init__(self, name, hunger = 0, color = "green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("raaawr")

    def breath_fire(self):
        print("$@#$#@$")




def main():
    zoo_lst = []
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst.extend([dog, cat, skunk, unicorn, dragon])
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)
    zoo_lst.extend([dog2, cat2, skunk2, unicorn2, dragon2])
    for animal in zoo_lst:
        if animal.is_hungry():
            print(str(type(animal).__name__) + " " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        else:
            animal.breath_fire()
    print("zoo name: " + zoo_lst[0].zoo_name)



if __name__ == '__main__':
    main()