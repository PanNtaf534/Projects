from caesar_cipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,mode):
    if mode == "encode":
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text = cipher_text + letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")
    elif mode == "decode":
        deciphered_text = ""
        for letter in original_text:
            if letter not in alphabet:
                deciphered_text = deciphered_text + letter
            else:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position = shifted_position % len(alphabet)
                deciphered_text = deciphered_text + alphabet[shifted_position]
        print(f"Here is the decoded result: {deciphered_text}")
    else:
        print("Wrong input.Please type again.")


end = False
while not end:# != True
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, mode=direction)
    while True:
        user_choice = input("Type 'yes' if you want to go again.Otherwise type 'no'.").lower()
        if user_choice == "yes":
            break
        elif user_choice == "no":
            end = True
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
