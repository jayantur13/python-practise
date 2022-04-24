from camelcase import CamelCase


def takeInput():
    namelist = []
    addmore = True
    while addmore:
        names = str(input("Enter name in list: \n"))
        namelist.append(names)
        addmore = str(input("Do you want to add more name ? (y/n) \n"))
        if addmore.lower() == 'y':
            addmore = True
        elif addmore.lower() == 'n':
            addmore = False
            toCamelCase(namelist)


def toCamelCase(namelist):
    c = CamelCase()
    lastlist = []
    for val in namelist:
        fdata = c.hump(val)
        lastlist.append(fdata)
    print(list(lastlist))


takeInput()
