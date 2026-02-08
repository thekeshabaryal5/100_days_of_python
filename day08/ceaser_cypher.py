import string
alphabet = list((string.ascii_lowercase))
is_on = True

def ceaser(message,shift,encode_or_decode):
    if encode_or_decode == "decode":
        shift *= -1
    for i in range(len(message)):
            if message[i] not in alphabet:
                continue
            else:
                original_index = alphabet.index(message[i])
                new_index = (original_index + shift)%len(alphabet)
                message[i] = alphabet[new_index]
    
    print(f"Your {encode_or_decode}d message is {"".join(message)}")
    
while is_on:
    operation = input("Type encode for encrypting and decode for decrypting. ").strip().lower()
    message = list(input("Enter your message: ").strip().lower())
    shift = int(input("Enter your shift number: "))%25
    ceaser(message,shift,operation)
    print("*"*25)
    
    play_again = input("Do you want to play again? y/n ").strip().lower()[0]
    if play_again!="y":
        print("Good bye")
        is_on = False