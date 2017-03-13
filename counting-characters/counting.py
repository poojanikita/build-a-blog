def countingchar(txt):
    dict = {}
    for i in txt:
        dict[i] = dict.get(i,0) + 1
    keylist = list(dict.keys())
    keylist = sorted(keylist)
    for x in range (len(keylist)):
        print(keylist[x],": ", dict[keylist[x]])


countingchar("Mary had a little LaMb")

for x in keylist:
    print(str(x) + ": " + str(dict[x]))
