print("Enter Integer1:")
Integer1 = input()
print("Enter Integer2:")
Integer2 = input()
Integer3 = (int(Integer1) % 2) + (int(Integer2) % 2)
if Integer3==0:
    print("Both numbers are even: True")
else: 
    print("Both numbers are even: False")    
if Integer3==2:
    print("At least one number is even: False")
else: 
    print("At least one number is even: True")     