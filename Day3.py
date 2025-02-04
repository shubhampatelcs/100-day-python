# Day 3 :
# Learning objective :
# conditional statement,logical operators and Code blocks nd scope:

# If else

# if condition :
#       do this
# else:
#       do this

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm ? "))

if height >= 120:
    print("you can ride this rollercoaster!")
else:
    print("Sorry ! You cannot  ride this rollercoaster for now !")

# comparison operator : >,<,>=,<=,==,!=

# Modulo Operator ( % ) : it gives reminder
# 10 % 2 = 0
# 10 % 3 = 1

number = int(input("what is number you want to check for odd and even? "))

if number % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")

# Nested if / else

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm ? "))
age = int(input("What is your age ? "))
bill=0

if height >= 120:
    if age >=18:
        print ("you can ride this rollercoaster and price for ticket is $12")
        bill=12
    else:
        print ("you can ride this rollercoaster and price for ticket is $7")
        bill=7

    wants_photo=input("Would you like to take photo? (y/n) ")
    if wants_photo == "y":
        bill=bill+3
        print("you added photos in your bill: " + str(bill))
    else:
        print("you added photos in your bill: " + str(bill))

else:
    print("Sorry ! You cannot  ride this rollercoaster for now !")

# Multiple IF :

# Logical operator :
# AND - both need to be true to be true
# OR - one of them need to be true to be true


