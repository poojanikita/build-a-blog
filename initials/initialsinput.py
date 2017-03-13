def get_initials_one(fullname):

    fullnm = (input("what is your name?"))
    fullnmlst = fullnm.split()
    intls = ""
    for ltrs in fullnmlst:
        intls = intls + ltrs[0]
    fullnmlst = " ".join(fullnmlst)
    final = "The initials of " + "'" + fullnmlst + " '" + " are " + intls.upper()
    return final
print(get_initials_one(""))
