# Write a program that takes an integer as input and prints out all the factors of that integer.


number = int(input("Enter the number : "))   
i = 0
while i < number:
   i += 1
   if number % i  == 0:
       print(i)

