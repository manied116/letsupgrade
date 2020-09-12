#tuple
fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
print(fruits)

# Tuple default methods

#access
fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
print(fruits[1])

#range
print(fruits[2:5])

#loop
fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
for x in fruits:
    print(x)

#check if item
fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
if "banana" in fruits:
    print("yes, 'banana is in the fruits tuple'")

#lenth
print(len(fruits))

#remove
fruits = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
del fruits
print(fruits)