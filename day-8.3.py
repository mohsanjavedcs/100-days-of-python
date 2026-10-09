alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
            shift *= -1
    for letter in text:
        if letter in alphabets:
            idx = alphabets.index(letter)
            shifted_idx = idx + shift
            end_letter = alphabets[shifted_idx]
            end_text += end_letter
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n").lower()
    if result == "no":
         should_continue = False
         print("Goodbye!")