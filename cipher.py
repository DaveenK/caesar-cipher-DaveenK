cipher_dict = {
    'a' : 'f',
    'b' : 'g',
    'c' : 'h',
    'd' : 'i',
    'e' : 'j',
    'f' : 'k',
    'g' : 'l',
    'h': 'm',
    'i' : 'n',
    'j' : 'o',
    'k': 'p',
    'l' : 'q',
    'm' : 'r',
    'n' : 's',
    'o' : 't',
    'p' : 'u',
    'q' : 'v',
    'r' : 'w',
    's' : 'x',
    't' : 'y',
    'u' : 'z',
    'v' : 'a',
    'w' : 'b',
    'x' : 'c',
    'y' : 'd',
    'z' : 'e',
}
result = ""
sentence = input("Please enter a sentence.")
lower_sentence = sentence.lower()
for character in lower_sentence:
    if character.isalpha():
        result += cipher_dict[character]
    else:
        result += character
print(result)