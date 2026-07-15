name = input("Your name : ")
age = int(input("your age : "))
hight = float(input("your hight :"))
power = int(input("your power : "))
money = int(input("your money : "))
if age >=30 and hight >=180 and power >=8 and money >=1000:
    print(name,"your pass")
    print("You are new CEO")
elif age >=20 and hight >=170 and power >=5 and money >=500:
    print(name,"your pass")
    print("You are new Employee")
elif age >=20 and hight >=160 and power >=3 and money >=250:
    print(name,"your pass")
    print("You are new clearer")
elif age <=20 and hight <=160 and power <=3 and money <=250:
    print(name,"You Not pass")
else:
    print(name,"you not pass")
        
