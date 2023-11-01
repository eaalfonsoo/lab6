
def encode(password):
    new_password = ""
    for i in range(len(password)):
        new_password += str((int(password[i]) + 3) % 10)
    return (new_password)


def main():
    while True:
        print("Menu")
        print("__________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))

        if option == 1:
            print("Your password has been encoded and stored")
        if option == 2:
           pass
            #print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}"
        if option == 3:
            break
if __name__ == "__main__":
    main()



