# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Set the variable for the combined names
#Set them both to lower and cocatenate them to combine them 
combined_names = name1.lower() + name2.lower()

#Set each letter to count to check for each letter in the combined names
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e


#Convert it to string as the names are now ints
love_score = str(true) + str(love)
true_love = int(love_score)
if (true_love < 10) or (true_love > 90):
  print("Your score is",true_love,",you go together like coke and mentos")

elif (true_love >= 40) and (true_love <= 50):
  print("Your score is",true_love,",you are alright together.")

else:
  print("Your score is", true_love)

