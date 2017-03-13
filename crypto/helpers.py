def alphabet_position(letter):
    lwr = "abcdefghijklmnopqrstuvwxyz"
    upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.islower():
        x = letter
        for letter in lwr:
            return lwr.index(x)
    elif letter.isupper():
        x = letter
        for letter in upr:
            return upr.index(x)


def rotate_character(char, rot):
    lwr = "abcdefghijklmnopqrstuvwxyz"
    upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rot = int(rot)
    if char.islower():
        new = char
        for new in lwr:
            indx = (alphabet_position(char)) + rot
            if indx < 26:
                pos = indx
            else:
                pos = (indx % 26)
            return lwr[pos]

    elif char.isupper():
        new = char
        for new in upr:
            indx = (alphabet_position(char)) + rot
            if indx < 26:
                pos = indx
            else:
                pos = (indx % 26)
            return upr[pos]
    else:
        return char
