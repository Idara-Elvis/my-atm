#creating a function that checks if the user input is a prime number or not

#collect user input


while True:
    number1 = int(input("please enter any number of your choice: "))
    if number1 < 1:
        continue
    elif number1 == 2:
        print(number1,"is a prime number")
        break
    else:
        for n in range(2, (number1)):
            if (number1 % n) == 0:
                print(number1,"is not a prime number")
                break
            print(number1,"is a prime number")
            break
    
                 
    