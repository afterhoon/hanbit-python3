# p125

import sys

print("Please input number : ")
a = int(input())

if a == 0 : # same 'if not a : '
    print("0 is impossible to divide")
    sys.exit(0)
    
print('3 / ', a, ' = ', 3/a)