# SUM OF ALL EVEN NUMBERS FROM 1 TO 100



sum=0
# for number in range(1,101):
#     if number%2==0:
#         sum+=number


# OR BY USING THE STEP PART OF THE RANGE FUNCTION

for number in range(2,101,2):
    sum+=number
print(sum)

