print("Welcome to the Love Calculator!")
name1=input("ENTER YOUR NAME : \n")
name2=input("ENTER YOUR LOVER'S NAME : \n")


new_name=name1+name2
lower_string=new_name.lower()

t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")
true=t+r+u+e

l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")

# print(f"T occurs {new_name.count("t")} times")
# print(f"R occurs {new_name.count("r")} times")
# print(f"U occurs {new_name.count("u")} times")
# print(f"E occurs {new_name.count("e")} times")

# true="true"
# count2=0
# print(f"L occurs {new_name.count("l")} times")
# print(f"O occurs {new_name.count("o")} times")
# print(f"V occurs {new_name.count("v")} times")
# print(f"E occurs {new_name.count("e")} times")

# love="love"

#THANKYOU!!!