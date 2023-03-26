# Task 1: Write a function that takes two parameters (a and b) and returns their sum.

# def sum(a, b) :
#     print ("a:", a)
#     print("b:", b)
#     suma = a + b
#     return suma 
# res = sum(7, 4)
# print("sum:", res)


# Task 2:Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string.
# Hint: you can use given_character in "aeiou"

# def Count_Vow(string, vowels) :
#     final = [each for each in string if each in vowels]
#     print (len(final))
#     print(final)

# string = "Cat on the roof" 
# vowels = "AaEeIiOoUu"
# Count_Vow(string, vowels) ;  


# Task 3:Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise

# def Function(string) :
#     return string == string[::-1]

# string = "savas"
# value = Function(string)
# if value:
#     print("True")
# else:
#     print("False")  



# Task 4:Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list

# def f(list) :
#     even_n = []
#     for i in list:
#       if i % 2 == 0:
#         even_n.append(i) 
#     return even_n

# even_n = f([1, 2 ,4, 6])
# print("Even numbers are:", even_n)   


# Task 5:Write a function that takes a list of integers and a target sum as parameters and returns
# a list of two integers from the original list that add up to the target sum.

# def Sum_numbers(integers :int, target_sum :int):
#     output = []
#     for i in integers:
#         if target_sum - i in integers:
#             output = [i, target_sum-i]
#             break
#     return output

# print(Sum_numbers([1,6,7,8,4,3],11))


# Task 6: Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list.

# def List(*numbers: int):
#     product = 1
#     for number in numbers:
#         product = product * number
#     return product

# print(List(2,3,6))


# Task 8:Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value.

# def Keys_even(**dic):
#     keys = []
#     for key in dic:
#         if dic.get(key) % 2 == 0:
#             keys.append(key)
#     return keys


# print(Keys_even(k1=1, k2=2, k3=7, k4=8))


# Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new dictionary
# that contains the sum of the values for each key in the original dictionaries.

# dict = [{"cows" : 5, "horses" : 3, "pigs" : 2, "dogs" : 6},
#         {"horses" : 6, "cow" : 8, "pigs" : 1, "dogs" : 9},
#         {"pigs" : 4, "horses" : 7, "cows" :5, "dogs" : 10}]

# result = {}
# for i in dict:
#     for k in i.keys():
#         result[k] = result.get(k, 0) + i[k] 
# print(result)


# Task 10:Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# new_tuple = list(thistuple)
# new_tuple[0], new_tuple[-1] = new_tuple[-1], new_tuple[0]
# print(new_tuple)



# Task 11:Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3.

def f(list):
    set2 = set()
    for i in list:
        if i % 3 != 0:
            set2.add(i)
    return set2
list = [1, 3, 5, 6, 8, 9, 10, 11]
print(f(list))