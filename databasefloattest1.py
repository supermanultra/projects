def floats():
    import os
    abc = True
    no = ("no", "nah", "No", "n")
    filesize = os.stat("database.txt").st_size
    if filesize == 0:
        with open('database.txt', 'a') as db:
            print("populatingfilesoitdoesntfail = 0.00", file=db)
    while abc:
        w = 1
        k = input("Write any item here to check if it floats in water: ")
        print()
        data = open('database.txt')
        answer = {}
        for line in data:
            m, v = line.strip().split('=')
            answer[m.strip()] = v.strip()
        data.close()
            
        if k in answer:
            update = input("Item '"+k + "' already exists in the database. Wanna update it's value? ")
            if update in no:
                print()
                if float(answer[k]) > 1:
                        print("The " + k + " will not float. You asked this already! ")
                        
                else:
                        print("The " + k + " will float. You asked this already!")
                        
            else:
                del answer[k]
                
        
        if k not in answer:
            print()
            l = float(input("Write the g/cm3 value here: "))
            print()

            if l >= w:
                print("The " + k + " will not float.")
                with open('database.txt', 'a') as database:
                    print(k + " = " + str(l), file=database)
            elif l < w:
                print("The " + k + " will float.")
                with open('database.txt', 'a') as database:
                    print(k + ' = ' + str(l), file=database)

        print()
        a = input("Wanna check another item? ")
        if a in no:
            abc = False
            print()
            print("To run this again type floats()")
        else:
            print()



floats()
