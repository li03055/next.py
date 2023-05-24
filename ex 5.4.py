
def check_id_valid(id_number):
    return sum(int(digit) if index % 2 == 0 else sum(map(int, str(int(digit) * 2))) for index, digit in
               enumerate(str(id_number))) % 10 == 0

#print(check_id_valid(123456780))
#print(check_id_valid(123456782))


class IDIterator:   # create iterator for id
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration
        while not check_id_valid(self._id):
            self._id += 1
        current_id = self._id
        self._id += 1
        return current_id


def id_generator(id):
    while id <= 999999999:  # until id reaches 999999999
        if check_id_valid(id):
            yield id
        id += 1


def main():
    user_id = input("Enter an ID: ")
    g_or_i = input("Generator or Iterator? (gen/it): ")
    if g_or_i == "gen":
        print("you chose generator")
        user_id_generator = id_generator(int(user_id))
        for i in range(10):
            print(next(user_id_generator))
    else:
        print("you chose iterator")
        user_id_iterator = IDIterator(int(user_id))
        for i in range(10):
            print(user_id_iterator.__next__())



if __name__ == '__main__':
    main()