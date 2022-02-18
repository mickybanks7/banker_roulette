# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

name1 = len(names)

name_rand = random.randint(0, name1 - 1)
name_check = names[name_rand]
print(name_check + ' is going to buy the meal today!')

