def avg():

    sum = 0
    count =0
    while count < 10:
        num1 = int(input('enter first number: '))
        #print(num1)
        count += 1
        sum +=num1
        #print(sum)
    avge =(sum/count)


    print(avge)

avg()