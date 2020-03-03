class calc:
    pass

    def product(self, num_1, num_2):
        return num_1 * num_2

    def sum(self, num_1, num_2):
        return num_1 + num_2

    def division(self, num_1, num_2):
        return num_1 / num_2

    def sub(self, num_1, num_2):
        return num_1 - num_2


# c = calc()
# print(c.product(5, 6))

def compute():
    c = calc()
    operator = input('''
        type math operator of choice:
        + for addition
        - for subtraction
        * for product
        / for division
        ''')

    num1 = int(input('enter first number: '))
    num2 = int(input('enter second number: '))

    if operator == "*":
        print(c.product(num1, num2))

    elif operator == "-":
        print(c.sub(num1, num2))
    elif operator == "+":
        print(c.sum(num1, num2))
    elif operator == "/":
        print(c.division(num1, num2))

    else:
        print("invalid")


def again():
    work_out = True
    while work_out:

        compute()

        choice = input('''
        perform another computation?
       y for yes or n for no.
       ''')
        if choice == 'y':
            work_out = True
            print('welcome back')
        else:
            work_out = False
            print('goodbye')


again()
