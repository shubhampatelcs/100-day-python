print("Welcome to Pizza Order")
size=input("what size pizza do you want? S,M or L : ")
pepperoni = input("do you want pepperoni?: y and n ")
extra_cheese = input("do you want extra cheese?: y and n ")

total_bill=0

if size == "S":
    total_bill=5
elif size == "M":
    total_bill=10
else:
    total_bill=15

if pepperoni == "y" and size == "S":
    total_bill+=2
else:
    total_bill+=3

if extra_cheese == "y":
    total_bill+=3

print(" your total bill is " + str(total_bill))