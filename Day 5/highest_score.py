scores=input("ENTER THE SCORES OF THE STUDENTS IN A LIST : ").split()
# print(scores)
length=len(scores)
for i in range(0,length):
    scores[i]=int(scores[i])
print(scores)

highest_score=0
for i in range(0,length):
    if scores[i]>highest_score:
        highest_score=scores[i]
print(f"The highest score in the class is : {highest_score} ")


# OR You can directly use the max() function

print(f"The highest score in the class is : {max(scores)} ")

# THERE ARE 2 TYPES OF COMPARISON FUNCTION TO FIND MAX OR MIN
# THEY ARE max(any_list_as_a_parameter) and min(any_list_as_a_parameter) 