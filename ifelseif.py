try:
    var = int(input("Your number:" ))
 
except ValueError as var_error:
    print("Please enter a number")
    print(var_error)

if var > 2:
    print("Your number is greater than 2")

elif var < 2:
    print("Your number is less than 2")
    