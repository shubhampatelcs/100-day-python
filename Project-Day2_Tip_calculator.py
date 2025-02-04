
print("Welcome to Tip Calculator!")
total_amount = float(input("What is your total amount?"))
tip_percent = float(input("How much tip would you like to give? 10,12 or 15 ?"))

total_people = int(input("How many people to split the bill ?"))

total_per_person = (total_amount + (total_amount*(tip_percent /100))) / total_people

print(f"Each Person Should pay : $ {round(total_per_person,2)}")