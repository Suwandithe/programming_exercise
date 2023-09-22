print("enter your height")
htInFeet = int (input("feet :"))
htInInches = int(input("inches :"))
heightInCm = (htInFeet * 12 + htInInches)*2.54
boardLen = (heightInCm*88)/100
print (f"suggested board length is {boardLen} cm")