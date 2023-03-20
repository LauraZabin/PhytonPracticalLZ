# Write the program to sort the list (without using sort function). You can implement any algorithm

list = ["Element4","ELement0","Element3", "Element1"]
# list.sort()
# print(list)

for i in range(len(list)):
    for j in range(i + 1, len(list)):

         if list[i] > list[j]:
             list[i], list[j] = list[j], list[i]
print(list)