print("Enter your age:")
age = input()
print("Do you have a driver's license:")
license = input()
# license = "yes"
if int(age) >= 18 and license == "yes":
   print("You are able to drive: True")
else:
    print("You are able to drive: False")   