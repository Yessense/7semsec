from collections import Counter
from caesar.caesar import alphabet
from caesar.caesar import caesar

with open('tihiy_don.txt', 'r', encoding='utf8') as f:
    text = f.read()

text = text.lower()
text = "".join([letter for letter in text if letter in alphabet])

freq = {'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.7, 'д': 2.98, 'е': 8.45, 'ё': 0.04, 'ж': 0.94, 'з': 1.65, 'и': 7.35,
        'й': 1.21, 'к': 3.49, 'л': 4.4, 'м': 3.21, 'н': 6.7, 'о': 10.97, 'п': 2.81, 'р': 4.73, 'с': 5.47, 'т': 6.26,
        'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48, 'ч': 1.44, 'ш': 0.73, 'щ': 0.36, 'ъ': 0.04, 'ы': 1.9, 'ь': 1.74,
        'э': 0.32, 'ю': 0.64, 'я': 2.01}

encoded_text = caesar(text, 'привет', shift=3, old_alphabet=alphabet)

encoded_text_counts = Counter(encoded_text)
normal_text_counts = Counter(text)

normal_frequencies_alphabet = "".join([k for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)])
normal_text_frequencies_alphabet = "".join([k for k, v in sorted(normal_text_counts.items(), key=lambda item: item[1], reverse=True)])
encoded_text_frequencies_alphabet = "".join([k for k, v in sorted(encoded_text_counts.items(), key=lambda item: item[1], reverse=True)])

decoded_text = "".join([normal_frequencies_alphabet[encoded_text_frequencies_alphabet.index(letter)] for letter in encoded_text])
print(decoded_text)
