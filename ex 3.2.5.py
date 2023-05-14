def read_file(file_name):
    try:
        with open (file_name, 'r') as file:
            print("__CONTENT_START__\n")
            print(file.read())
    except:
        print("__CONTENT_START__\n" + "")
        print("__NO_SUCH_FILE__")
    finally:
        print("\n__CONTENT_END__")

read_file("words.txt")
read_file("lior.txt")