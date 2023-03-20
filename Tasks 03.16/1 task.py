# Ask the user to enter the text and a letter. Count how many occurrences of the letter provided.

text = input("Enter the text\n")
# letter = input("Enter the letter\n")
# occur = text.count(letter)
# print("Count of" , letter , "is" , str(occur))


#  Based on the task 1, count the occurrences of each character in the text provided and display them in the output
mytext = set(text)
for element in mytext:
    countOfChar = 0
    for character in text:
        if character == element:
            countOfChar += 1
    print("Count of character '{}' is {}".format(element, countOfChar))
