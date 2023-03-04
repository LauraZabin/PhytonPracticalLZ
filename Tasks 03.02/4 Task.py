print("Enter a year:")
year = input()
leap1 = int(year) % 4
leap2 = int(year) % 100
leap3 = int(year) % 400
if (leap1 == 0 and leap2 > 0) or leap3 == 0:
    print("Leap year: True")
else:
    print("Leap year: False")