MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}



def user_type():
    again = input("Want to encrypt or decrypt another string? type 'yes' or 'no'\n").lower()
    if again == "yes":
        select_mode()
    elif again == "no":
        print("Goodbye.")
    else:
        print("JIJIJIJA")
        user_type()


def select_mode():
    print("Welcome to the morse translator!")
    selected_mode = input("Please write the mode you want to select. modes available 'decrypt' and 'encrypt'\n")
    if selected_mode == "decrypt":
        decrypt_morse()
    elif selected_mode == "encrypt":
        encrypt_to_morse()
    else:
        print("\n")
        print("Please provide a valid mode...")
        print("\n")
        select_mode()



def decrypt_morse():
    string_to_convert = input("Please write morse code to convert it to Natural Language!\n").upper() + " "
    converted_string = ""
    converted_list = []
    i = ""
    
    for char in string_to_convert:
        if char == " ":
            try:   
                converted_list.append(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(i)])
            except:
                pass
            converted_list.append(" ")
            i = ""
        else:
            i += f"{char}"
    
    for letter in converted_list:
        converted_string += letter    
        
    print(converted_string)

    user_type()


def encrypt_to_morse():
    string_to_convert = input("Please write a string to convert it to Morse Code!\n").upper()
    converted_string = ""

    converted_list = [MORSE_CODE_DICT.get(char, "None") for char in string_to_convert]

    for code in converted_list:
        converted_string += f"{code} "

    if "None" in converted_string:
        converted_string = converted_string.replace('None', " ")

    print(converted_string)

    user_type()


select_mode()
