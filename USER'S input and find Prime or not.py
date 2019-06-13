# a prime number is one that can only be divided by it self or 1
# while all other numbers are divided by either 2 or 3


for x in range(0,6,1) :

    number = int(input("\n\nenter any number :\n \n ---->"))

    if number == 0 :
            print ('NOT A PRIME NUMBER')

    elif number % number ==0 and number % 1 ==0 :


        if number ==2 :
            print("PRIME NUMBER")


        elif number ==3 :
            print('PRIME NUMBER')


        elif number %2 !=0 and number %3 !=0 :
            print('PRIME NUMBER')


        else :
            print("NOT A PRIME NUMBER")
