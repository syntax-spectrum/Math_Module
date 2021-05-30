#Zachary Baird
#Date: 08/16/2020
#Description: Application prompts user to enter two integers
#           to be modified based on the math module.

from math import gcd, remainder, pow

#Functions
def gcd_func(x, y):
#Greatest Common Denominator function from the math module
    result = gcd(x, y)
    return result
def remainder_func(x, y):
#Remainder function from the math module
    result = remainder(x, y)
    return result
def power_func(x, y):
#Power function from the math module
    result = pow(x, y)
    return result

#Main
choice = 0
quitter = ' '

while quitter != 'Quit' and quitter != 'quit':
    x = int(input('Please enter your first value for \'x\': '))
    y = int(input('Please enter your second value for \'y\': '))
#User Choice
    while choice == 0:
        choice = int(input('\nEnter: \n1. Greatest Common Denominator\n2. Remainder\n3. Power\nChoice: '))

        if choice == 1:
            answer = gcd_func(x, y)
            break
        elif choice == 2:
            answer = remainder_func(x, y)
            break
        elif choice == 3:
            answer = power_func(x, y)
            break
        else:
            choice == 0
            print('Please enter a valid choice, ')
            continue
#Output
    print('The result of the variables for ', x, ' and ', y, ' is ', answer)
    choice = 0
    quitter = input('Enter \'Quit\' to quit, else \'enter\' to continue: ')
