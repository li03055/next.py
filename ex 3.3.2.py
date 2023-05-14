class UnderAge(Exception):
    def __str__(self):
        return "Your age is {} which is less than 18. You need to wait {} more years to attend Ido's birthday".format(self.age, 18 - self.age)

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        e.age = int(age)
        print(e)


send_invitation("John", 20)
send_invitation("Alice", 16)
