print("Enter year:")
year = input()
print("Enter month")
month = input()
print("Enter day")
day = input()
leap_year=int(0)
leap1 = int(year) % 4
leap2 = int(year) % 100
leap3 = int(year) % 400
if (leap1 == 0 and leap2 > 0) or leap3 == 0:
   leap_year=1
if (int(year) >= 0 and int(year) < 9999) and (0 < int(month) < 13) and ((0 < int(day) < 31 and int(month) != 2) or (int(month) in (1, 3, 5, 7, 8, 10, 12) and int(day) == 31 and int(month) != 2) or (int(month) == 2 and int(day) <29) or((int(month) == 2 and int(day) == 29 and int(leap_year) == 1 ))):
     print("Date valid: True")
else:
     print("Date valid: False")  