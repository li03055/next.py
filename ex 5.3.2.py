class MusicNotes:
    def __init__(self):
        self.notes = {
            "la": [55, 110, 220, 440, 880],
            "si": [61.74, 123.48, 246.96, 493.92, 987.84],
            "do": [65.41, 130.82, 261.64, 523.28, 1046.56],
            "re": [73.42, 146.84, 293.68, 587.36, 1174.72],
            "mi": [82.41, 164.82, 329.64, 659.28, 1318.56],
            "fa": [87.31, 174.62, 349.24, 698.48, 1396.96],
            "sol": [98, 196, 392, 784, 1568],
        }
        self.notes_list = []
        for octave in range(5):
            for note in self.notes.values():
                self.notes_list.append(note[octave])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.notes_list):
            raise StopIteration
        frequency = self.notes_list[self.index]
        self.index += 1
        return frequency


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
