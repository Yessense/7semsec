import string

alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alphabet = alphabet_lower


def create_new_alphabet(key_word: str, shift: int, old_alphabet: str) -> str:
    without_key = [letter for letter in old_alphabet if letter not in key_word]
    new_alphabet = list(without_key[-shift:]) + list(key_word) + list(without_key[:-shift])
    new_alphabet = "".join(new_alphabet)
    return new_alphabet


def caesar(word: str, key_word, shift: int, old_alphabet: str) -> str:
    new_alphabet = create_new_alphabet(key_word=key_word,
                                       shift=shift,
                                       old_alphabet=old_alphabet)
    new_word = "".join([new_alphabet[old_alphabet.index(letter)] for letter in word])
    return new_word


def example_usage():
    old_alphabet = alphabet
    new_alphabet = create_new_alphabet(key_word='привет', shift=3, old_alphabet=alphabet)

    encoded_word =  caesar('привет', key_word='привет', shift=3, old_alphabet=alphabet)


    print("Done")



if __name__ == '__main__':
    example_usage()
