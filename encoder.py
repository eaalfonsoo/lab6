#Emerson's encode function
def encode(password):
    new_password = ""
    for i in range(len(password)):
        new_password += str((int(password[i]) + 3) % 10)
    return new_password


def decode(password):
    decoded_pass = ''
    for x in range(len(password)):
        decoded_pass += str((int(password[x]) - 3) % 10)
    return decoded_pass


def main():
    while True:
        print("Menu")
        print("__________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))

        if option == 1:
            user_password = input('Please enter your password to encode: ')
            encoded = encode(user_password)
            print("Your password has been encoded and stored")
        if option == 2:
            print(f'The encoded password is {encode(user_password)}, and the original password is {decode(encoded)}.\n')
        if option == 3:
            break


if __name__ == "__main__":
    main()



