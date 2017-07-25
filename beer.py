word = "bottles"

for beernum in range(99, 0,-1):
    print(beernum, word, "of beer on the wall.")
    print(beernum, word, "of beer.")
    print("Take one down")
    print("Pass it around")
    if beernum == 1:
        print("No more bottles of beer on the wall")
    else:
        new_num = beernum - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall")
   
    print()
