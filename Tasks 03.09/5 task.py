# Write a program that takes an integer as input and prints out whether that integer is prime or not.
        
number = int(input("Enter the number : "))   
i = 2
while i < number:
   if number % i  == 0:
       break
   else: i = i + 1
if number == i and number > 1 and number % 1 == 0:
    print("Pirminis")
else: print ("NEpirminis")






