def floats():
    abc = True
    no = ("no", "nah", "No", "n")
    while abc:
        k = input("Write any item here to check if it floats in water: ")
        print()
        l = float(input("Write the g/cm3 value here: "))
        print()
        w = 1
        if l > w:
            print("The " + k + " will not float.")
        if l < w:
            print("The " + k + " will float.")
        print()
        a = input("Wanna check another item? ")
        if a in no:
            abc = False
            print()
            print("To run this again type floats()")
        else:
            print()



floats()




def float_check(item, density):
    water = 1
    if density > water:
        return("The" + item + "will not float in water! :(")

    else:
        return("The " + item + " will float in water! :)")
        
