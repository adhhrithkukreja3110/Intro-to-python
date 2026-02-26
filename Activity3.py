print("Enter Marks Obtained in 4 Subjects:")
math = int(input("math: "))
science = int(input("science: "))
english = int(input("english: "))
hindi = int(input("hindi: "))



sum = math + science + english + hindi
print("The sum of maths,science,english,hindi is: ", sum)

perc = (sum / 400) *100

print(end ="Percentage Marks: ")
print(perc)