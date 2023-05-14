password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
def main(password):
    return lambda password: ''.join(chr(ord(char) + 2) if char.isalpha() else char for char in password)

decoded_sentence = main(password)(password)  
print(decoded_sentence)