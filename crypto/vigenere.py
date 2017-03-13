from helpers import alphabet_position, rotate_character


def encrypt(text,key):

    encrypted = ""
    keypos = 0
    startpos = 0
    for c in text:
        if c.isalpha() != True:
            encrypted = encrypted + c
            startpos = startpos - 1
        else:
            akey = alphabet_position(key[startpos])
            rotated = rotate_character(c,akey)
            encrypted = encrypted + str(rotated)

        if startpos == (len(key) - 1):
            startpos = 0
        else:
            startpos += 1
    return encrypted






def main():
    text = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(text,key))

if __name__ == "__main__":
    main()
