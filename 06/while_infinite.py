# p132

while True :
    print("You want repeat continue?[Y/N] : ")
    answer = input()
    
    if answer == 'Y' or answer == 'y' :
        print("Repeat continue")
    elif answer == 'N' or answer == 'n' :
        print("Repeat has ended")
        break
    else :
        print("Invalid answer")