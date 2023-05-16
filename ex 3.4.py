import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char_in_username, index_of_char):
        self.char_in_username = char_in_username
        self.index_of_char = index_of_char
    def __str__(self):
        return f"Username contains illegal character: '{self.char_in_username}' in index: {self.index_of_char}"

class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is less than 3 characters"

class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is more than 16 characters"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password is missing at least one must be character"

class PasswordMissingUpper(PasswordMissingCharacter):
    def __str__(self):
        return "Password is missing a character (Uppercase)"

class PasswordMissingLower(PasswordMissingCharacter):
    def __str__(self):
        return "Password is missing a character (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return "Password is missing a character (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return "Password is missing a character (Special)"

class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is less than 8 characters"

class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is more than 40 characters"

def check_input(username, password):
    if not (3 <= len(username) <= 16):  # check len of username
        if len(username) < 3:
            raise UsernameTooShort()
        if len(username) > 16:
            raise UsernameTooLong()
    if not (8 <= len(password) <= 40):  # check len of password
        if len(password) < 8:
            raise PasswordTooShort()
        if len(password) > 40:
            raise PasswordTooLong()
    username_chars = string.ascii_letters + string.digits + "_"    # username must be with english letters, digits and underscore
    if not all(char in username_chars for char in username):    # check if username is legal
        illegal_char = next(char for char in username if char not in username_chars)
        index_of_char = username.index(illegal_char)
        raise UsernameContainsIllegalCharacter(illegal_char, index_of_char)
    if not any(char in string.ascii_lowercase for char in password):    # check if password has at least one little letter
        raise PasswordMissingLower()
    if not any(char in string.ascii_uppercase for char in password):    # check if password has at least one upper letter
        raise PasswordMissingUpper()
    if not any(char in string.digits for char in password):     # check if password has at least one digit
        raise PasswordMissingDigit()
    if not any(char in string.punctuation for char in password):    # check if password has at least one special sign
        raise PasswordMissingSpecial()
    print("OK :)")
    return True



#print(check_input("1", "2"))
#print(check_input("0123456789ABCDEFG", "2"))
#print(check_input("A_a1.", "12345678"))
#print(check_input("A_1", "2"))
#print(check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"))
#print(check_input("A_1", "abcdefghijklmnop"))
#print(check_input("A_1", "ABCDEFGHIJLKMNOP"))
#print(check_input("A_1", "ABCDEFGhijklmnop"))
#print(check_input("A_1", "4BCD3F6h1jk1mn0p"))
#print(check_input("A_1", "4BCD3F6.1jk1mn0p"))

def main():

    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
            print(e)
            print("Please try again")
    print("Welcome!")


if __name__ == '__main__':
    main()