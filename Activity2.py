amount =int(input("Enter the amount for withdraw : "))



note_1 = amount//500
note_2 =(amount%500)//100
note_3 =((amount%500)%100)//50
note_4 =(((amount%500)%100)%50)//10

print("Number of 500 notes:", note_1)
print("Number of 100 notes:", note_2)
print("Number of 50 notes:", note_3)
print("Number of 10 notes:", note_4)