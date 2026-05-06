
number = int(input("Enter the number :"))

temp_number = number 
digit_count = 0


while temp_number > 0:
    digit_count += 1 
    temp_number //= 10


if digit_count >= 4:
    middle_index = digit_count // 2
    position = 0 

    while number > 0:
        digit = number % 10

        if position == middle_index:
            middle_digit_1 = digit
        elif position ==  middle_index - 1:
            middle_digit_2 = digit

        number //= 10
        position += 1

    product = middle_digit_1 * middle_digit_2

    print(f"\nProduct of middle digits({middle_digit_1} * {middle_digit_2}) = {product}")

else: 
    print("\nIt's not a 4- digit number !")