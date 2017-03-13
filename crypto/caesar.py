from helpers import alphabet_position, rotate_character
def encrypt(text, rot):

    encrypted = ''
    for c in text:
        if c == ' ':
            encrypted = encrypted + ' '
        else:
            rotated = rotate_character(c,rot)
            encrypted = encrypted + str(rotated)
    return encrypted


def main():
    text = input("Type a message:")
    rot = input("Rotate by:")
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
