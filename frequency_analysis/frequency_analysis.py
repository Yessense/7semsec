from collections import Counter
from caesar.caesar import alphabet
from caesar.caesar import caesar

# --------------------------------------------------
# Utils
# --------------------------------------------------
FREQ = {'о': 110305, 'а': 89283, 'е': 78621, 'и': 71524, 'н': 63271, 'л': 55232, 'т': 53704, 'с': 52889, 'р': 51396,
        'в': 48817, 'к': 42748, 'у': 34695, 'п': 31763, 'д': 30651, 'м': 29729, 'я': 23205, 'г': 22135, 'ы': 21458,
        'з': 19298, 'ь': 18621, 'б': 17001, 'й': 15603, 'ч': 14290, 'ш': 12354, 'х': 11406, 'ж': 9292, 'ю': 6596,
        'ц': 5136, 'щ': 3123, 'ф': 1635, 'э': 1444, 'ъ': 317}

def find_top_n_bigrams(text, top_n):
    new_text = [text[i:i + 2] for i in range(len(text) - 1)]
    bigrams_count = Counter(new_text)
    return bigrams_count.most_common(top_n)

# --------------------------------------------------
# Load file
# --------------------------------------------------

with open('tihiy_don.txt', 'r', encoding='utf8') as f:
    text = f.read()

text = text.lower()
text = "".join([letter for letter in text if letter in alphabet])

# --------------------------------------------------
# Encode text
# --------------------------------------------------

encoded_text = caesar(text, 'привет', shift=3, old_alphabet=alphabet)

# --------------------------------------------------
# Decode 1-grams
# --------------------------------------------------

encoded_text_counts = Counter(encoded_text)
normal_text_counts = Counter(text)

normal_frequencies_alphabet = "".join([k for k, v in sorted(FREQ.items(), key=lambda item: item[1], reverse=True)])
normal_text_frequencies_alphabet = "".join(
    [k for k, v in sorted(normal_text_counts.items(), key=lambda item: item[1], reverse=True)])
encoded_text_frequencies_alphabet = "".join(
    [k for k, v in sorted(encoded_text_counts.items(), key=lambda item: item[1], reverse=True)])

decoded_text = "".join(
    [normal_frequencies_alphabet[encoded_text_frequencies_alphabet.index(letter)] for letter in encoded_text])

# --------------------------------------------------
# Decode bi-grams
# --------------------------------------------------

bigrams_count = find_top_n_bigrams(text, 10)
bigrams_decoded_text = find_top_n_bigrams(decoded_text, 10)

for i in range(10):
    decoded_text.replace(bigrams_decoded_text[i][0], bigrams_count[i][0])

# --------------------------------------------------
# Print result
# --------------------------------------------------

print(decoded_text)
