height = float(input("enter your height is cm"))
weight = float(input("enter your weight is kg"))

BMI = weight / (height/100)**2

print(" your BMI is ", round(BMI,2))

if BMI <= 18.4:
    print("you are under weight")    
elif  BMI <= 24.9:
    print("you are healthy")
elif  BMI <= 29.9:
    print("you are over weight ")
elif BMI <= 34.9:
    print("you are severly over weight")
elif BMI <= 39.9:
    print("you are obese ")
else:
    print("you are  severly obese ")