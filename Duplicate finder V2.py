# Duplicate Finder
# by Leo R.
from collections import Counter
import pyperclip

print("This tool lets you test for duplicates in any column you paste in\n")
repeat = 'y'

while repeat == 'y':
    print("Paste items")
    print("After last item hit enter, then spell out stop, hit enter again:\n")
    clm = []
    # this iteration adds iputs until you spell out stop:
    for line in iter(input, 'stop'):
        #print("You entered:", line)
        clm.append(line)

    print("raw input:",clm)
    clmlist = list(filter(None, clm))
    print("filtered: ",clmlist)
    print("\nTotal elements: ", len(clmlist))
    # Count and print duplicates
    counts = Counter(clmlist)
    dpl = {elem: cnt for elem, cnt in counts.items() if cnt > 1}
    unique = {elem: cnt for elem, cnt in counts.items() if cnt == 1}
    if len(dpl)>0:
        print("Total nbr. duplicates:", len(dpl))
        print("Total nbr. Uniques:", len(unique))
        print("Total nbr. Combined:", len(dpl)+len(unique))
        choice = input("Choice: 1 = Duplicates List, 2 = Uniques List, 3 = Combined List ")
        if choice == "1":
            print("Duplicates:      ")
            for j in dpl: print(j,": ",dpl[j])
            print("Total nbr. duplicates:", len(dpl))
        if choice == "2":
            print("Unique:      ")
            for i in unique: print(i)
            print("Total nbr. Uniques:", len(unique))
        else:
            print("Combined list:      ")
            for i in unique: print(i)
            for j in dpl: print(j)
            print("Total nbr. Combined:", len(dpl)+len(unique))
            #pyperclip.copy(unique+dpl)
        
    else:
        seelst = input("All entries unique. No duplicates found. want a list of all items?: ")
        if seelst == 'y':
            clmlist.sort()
            for i in clmlist:
                print(i)
    repeat = input("Wanna repeat? y/n: ")
