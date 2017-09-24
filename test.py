print("Enter the number of repetitions : ")
repeat = int(input())

if repeat > 0:
    print('')
    for i in range(1, repeat + 1):
        for j in range(i):
            print('*', end='')
        print('')
else:
    print("You can not a number less than or equal a 0.")