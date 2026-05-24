
# print(ord('A'))     # Output: 65

# print(ord('a'))     # Output: 97

# print(ord('0'))     # Output: 48

# print(ord('@'))     # Output: 64

# print(chr(65))      # Output: A

# print(chr(97))      # Output: a


char = input("Enter a single character: ")



if type(char) is str and len(char) == 1:
    print(" ")
else:
    print("Please enter exactly ONE character!")
ascii_val = ord(char)

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")

if ascii_val >= 65 and ascii_val <= 90:

    print(" Uppercase Letter")

elif ascii_val >= 97 and ascii_val <= 122:

    print(" Lowercase Letter")

elif ascii_val >= 48 and ascii_val <= 57:

    print(" Digit")

elif ascii_val == 32:

    print(" Space")

else:

    print(" Special Character")
# print("ASCII Value Checker")

# print("=" * 40)

# char = input("Enter a single character: ")


# if type(char) is str and len(char) == 1:

#     ascii_val = ord(char)  

#     print(f"\nCharacter: '{char}'")

#     print(f"ASCII Value: {ascii_val}")

#     print("\nCharacter Type: ", end="")

#     if ascii_val >= 65 and ascii_val <= 90:

#         print("Uppercase Letter")

#     elif ascii_val >= 97 and ascii_val <= 122:

#         print("Lowercase Letter")

#     elif ascii_val >= 48 and ascii_val <= 57:

#         print("Digit")

#     elif ascii_val == 32:

#         print("Space")

#     else:

#         print("Special Character")