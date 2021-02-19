#!C:\Users\ASUS\AppData\Local\Programs\Python\Python39\python

# All imports go here
from numbers import Number
from collections import deque
import string

# Function which changes the number to the required base
def change_base(number, base, map_data = string.digits + string.ascii_uppercase):
    if not (isinstance(number, Number) and not isinstance(number, complex)):
        raise TypeError('Number passed must be a real number')
    elif base < 2 :
        raise ValueError('Base must atleast have a value of 2')
    elif number == 0:
        return 0
    else:
        sign = -1 if number < 0 else 1
        number *= sign
        dq = deque()
        while number > 0:
            number, mod = divmod(number, base)
            dq.appendleft(mod)
        answer = ''.join(map_data[num] for num in dq)
        return answer if sign==1 else f'-{answer}'

if '__name__' !='__main__':
	number = int(input('Enter the number you wish to convert : '))
	base = int(input('Enter the base to which you need to convert to : '))
	print (f'Base 10 : {number} , Base {base} : {change_base(number, base)}')