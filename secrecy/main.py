from secrecy import Secrecy

encoder = Secrecy()


def main():
    message = input("Message: ")
    key = input("Key (number between 1 and {}): ".format(len(encoder.characters)))
    new_message = encoder.encode(message, key)
    print("New message: {}".format(new_message))


if __name__ == '__main__':
    main()
