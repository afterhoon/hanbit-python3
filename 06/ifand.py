# p128

print("Input number : ")
num = int(input())

if num > 10 and num % 2 :
    print("Beyond 10 odd number")
elif num > 10 and ~(num % 2) :
    print("Beyond 10 even number")
elif num % 2 :
    print("Below 10 odd number")
else :
    print("Below 10 even number")