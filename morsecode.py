morse_dictionary = """'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'"""

# print(morse_dictionary)

def generate_morse_code():
    morse_code = []
    morse_list = morse_dictionary.split(",")
    for s in morse_list:
        temp_str=""
        for i in range(len(s)):
                if s[i] == "'" or s[i] == ":" or s[i] == " ":
                    continue
                else:
                    temp_str += s[i]
        morse_code.append(temp_str)
    return morse_code

def convert_morse_char(morse_char):
    morse_code = generate_morse_code()
    for morse_letter in morse_code:
        for i in range(len(morse_letter)):
            if i == 0 and morse_letter[i] == morse_char:
                return morse_letter[1:len(morse_letter)]



def convert_morse_phrase(morse_phrase):
    morse_sen = ""
    for morse_char in morse_phrase:
        if morse_char != " ":
            morse_sen += convert_morse_char(morse_char)
    return morse_sen

input_sen = input("ENTER YOUR SENTENCE FOR MORSE CODE CONVERSION :")

print(convert_morse_phrase(input_sen))













#print(morse_list)

