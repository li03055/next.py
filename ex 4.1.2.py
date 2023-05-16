def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    words_generator = (words.get(word) for word in sentence.split())
    for word in words_generator:
        print(word)

translate("el gato esta en la casa")