#data structures and algorithms
#Strings, lists,sets,tuples and dictionaries
# Strings and lists
#1. Write a program to count the number of vowels and consonants in a string
vowels = ["a","e","i","o","u"]
consonents = ["a","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
print(len(f"{vowels},{consonents}"))
# 2.Reverse a string without using slicing ([::-1]).
word = "Hello World"
print("".join(reversed(word)))
# check whether the given string is palindrom or not
word = "madam"

if word == word [::-1]:
    print("it is a palindrom ")
else:
    print("it is not a palindrom ")
# Find the longest word in a sentence.
sentence = "Hello python"
word = sentence.split(" ")
for words in word:
    print(words,len(words))
# finging the lowest value in element
my_array  = [12,11,10,2,19,45]
my_val = my_array[0]
for i in my_array:
    if i < my_val:
        my_val = i
print("The lowest number in array is: ",my_val)
# ACCESSING THE LIST
# print secong item of list
list = [12,23,34,16]
print(list[1])
# print the last item of the list
list_1 = [12,23,34,10]
print(list_1[-1])
# return third,fourth and fifth item
list_2 = ["orange","apple","banana","pine","promogranate","papaya","kiwi","pear"]
print(list_2[2:5])
# return the give items but not including kiwi
print(list_2[:6])
# return the items from pine to end
print(list_2[3:])
# checking if item exists
print("kiwi" in list_2)
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
list_2[2:4] = ["blackcurrant","watermelon"]
print(list_2)
