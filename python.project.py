import random
a=random.randint(1,5)
count1=0
for i in range(3):
b=int(input("Enter a number between 1 to 5: "))

if b==a:
print("Right!")
count1+=1
else:
print("Wrong!")

else:
print("The computer generated number was:",a)
print("Your score is:",count1)
