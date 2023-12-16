height_of_students=input("Input a list of student heights : ")
student_height=height_of_students.split()

length=len(student_height)
for i in range(0,length):
    student_height[i]=int(student_height[i])
print(student_height)
# print(sum)

# METHOD - 1
# sum=0 
# for i in range(0,length):
#     sum+=student_height[i]
# average_height=round(sum/length)
# print(f"The average height of the students in the class is : {average_height} ")

# METHOD - 2
sum=0
for i in student_height:
    sum+=i
average=round(sum/length)
print(f"The average height of the students in the class is : {average} ")

# METHOD - 3

# sum=sum(student_height)
# print(sum)
# average=round(sum/length)
# print(f"THE AVERAGE HEIGHT OF THE STUDENTS IS : {average}")