alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(encrypt_or_decrypt):
    if encrypt_or_decrypt == "encode":

        #Encoding the message entered by the user.
        def encrypt(original_text, shift_amount):
            encoded_text = ""
            for count_letter in original_text:
                if count_letter == " ":
                    encoded_text += "_"

                elif count_letter not in alphabet:
                    encoded_text += count_letter

                elif count_letter != " ":
                    index_holder = alphabet.index(count_letter) + shift_amount
                    index_holder = index_holder % len(alphabet)
                    encoded_text += alphabet[index_holder]                                      

            print(f"Here is the encoded result: {encoded_text}")

        encrypt(text, shift)
    elif encrypt_or_decrypt == "decode":

        #Decoding the encrypted message given by the user.
        def decrypt(original_text, shift_amount):
            decoded_text = ""
            for count_letter in original_text:
                if count_letter == "_":
                    decoded_text += " "

                elif count_letter not in alphabet:
                    decoded_text += count_letter

                elif count_letter != "_":
                    index_holder = alphabet.index(count_letter) - shift_amount
                    index_holder = index_holder % len(alphabet)
                    decoded_text += alphabet[index_holder]

            print(f"Here is the decode result: {decoded_text}")

        decrypt(text, shift)
    else:
        print("_____Wrong input, 'Choose encode or decode.' Try again Please!_____")

process = True
while process:
    direction = input("Type 'encode' to encrypt, Type 'decode to decrypt'\n").lower()
    text = str(input("Type your message!:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction)

    restart = input("Type 'Yes' if you want to continue or Type 'No' if you want to exit!\n").lower()
    if restart == "no":
        print("Good Bye!!")
        process = False