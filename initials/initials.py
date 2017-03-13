def get_initials(fullname):

    fullnmlst = fullname.split()
    intls = ""
    for ltrs in fullnmlst:
        intls = intls + ltrs[0]
    return intls.upper()

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))
if __name__ == '__main__':
    main()
