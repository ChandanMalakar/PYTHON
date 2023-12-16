row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# print(map)
position=input("Where do you want to put the treasure? ")


column=int(position[0]) #column=3
row=int(position[1]) #row=1

# selected_row=map[row-1]
# selected_row[column-1]="X"

# Other way to do it is :
map[row-1][column-1]="X"

print(f"{row1}\n{row2}\n{row3}")
