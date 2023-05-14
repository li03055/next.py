def targil1():
    with open('names.txt') as file:
        print(max(file.read().splitlines(), key=len))

targil1()

def targil2():
    with open('names.txt') as file:
        print(sum([len(name.strip()) for name in file]))

targil2()


def targil3():
    with open('names.txt') as file:
        shortest_length = min(len(name.strip()) for name in file)
        file.seek(0)    # resets the file pointer back to the beginning of the file
        print(*(name.strip() for name in file if len(name.strip()) == shortest_length), sep='\n')

targil3()

def targil4():
    with open('names.txt') as input_file, open('name_length.txt', 'w') as output_file:
        output_file.writelines(str(len(name.strip())) + '\n' for name in input_file)

targil4()

def targil5():
    with open('names.txt') as file:
        num = int(input("enter a length: "))
        print(*(name.strip() for name in file if len(name.strip()) == num), sep='\n')

targil5()

