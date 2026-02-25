name = "penguin"
age = 15
is_student = True
weight = 38.5



print("Name:", name)
print("DataType of name is :", type(name))

print("Age:", age)
print("DataType of age is :", type(age))

print("Is Student:", is_student)
print("DataType of is_student is :", type(is_student))

print("Weight:", weight)
print("DataType of weight is :", type(weight))


print("\n After Type Casting.......\n")
age = str(age)
print(age)
print("DataType of age is :", type(age))
weight= int(weight)
print(weight)
print("DataType of weight is :", type(weight))