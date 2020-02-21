def compute():
    operator = input('''
    type math operator of choice:
    + for addition
    - for subtraction
    * for multipliction
    / for division
    ''')

    num1 = int(input('enter first number: '))
    num2 = int(input('enter second number: '))

    if operator == '+':
        print(num1 + num2)

    elif operator == '-':
        print(num1 - num2)

    elif operator == '*':
        print(num1 * num2)

    elif operator == '/':
        print(num1 / num2)
    else:
        print('invalid')


compute()

def again():
    compute_again = input('''
    perform another computation?
    y for yes or n for no.
    ''')

    if compute_again =='y':
        print('welcome back')
        compute()
    elif compute_again =='n':
        print('goodbye')

    else:
        print('power off')

again()