# new_string=input("Enter the names of the vegetables with pesiticides in an ascending order with commas and space \n")
# new_str=new_string.split(", ")
# print(new_str)

# dirty_dozen=['Strawberry', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
# print(dirty_dozen)

#now the main list is dirty_dozen here which contains both fruits and vegetables , but this is a long method

fruits=["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables=["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#here both the lists fruits and vegetables are present in the main list dirty_dozen

#shortening the main list dirty_dozen

dirty_dozen=[fruits, vegetables]
print(dirty_dozen)