a = int(input("Enter a value: "))
b = int(input("Enter a value 2: "))
c = int(input("Enter a value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is greater than %d, %d and %d" % (avg, a, b, c))
elif avg > a and avg > b and avg < c:
    print("%d is greater than %d and %d but less than %d" % (avg, a, b, c))
elif avg > a and avg < b and avg > c:
    print("%d is greater than %d and %d but less than %d" % (avg, a, c, b))
elif avg > a and avg < b and avg < c:
    print("%d is greater than %d but less than %d and %d" % (avg, a, b, c))
elif avg < a and avg > b and avg > c:
    print("%d is greater than %d and %d but less than %d" % (avg, b, c, a))
elif avg < a and avg > b and avg < c:
    print("%d is greater than %d but less than %d and %d" % (avg, b, a, c))
elif avg < a and avg < b and avg > c:
    print("%d is greater than %d but less than %d and %d" % (avg, c, a, b))
else:
    print("INVALID INPUT")