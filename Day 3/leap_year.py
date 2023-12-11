year=int(input("Enter a year:"))

# if year%4==0 and year%100!=0:
#     print(f"THE YEAR {year}, IS A LEAP YEAR")
# elif year%100==0 and year%400==0:
#     print(f"THE YEAR {year}, IS A LEAP YEAR")
# else:
#     print(f"THE YEAR {year}, IS NOT A LEAP YEAR")


if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"THE YEAR {year}, IS A LEAP YEAR")
        else:
            print(f"THE YEAR {year}, IS NOT A LEAP YEAR")
    else:
        print(f"THE YEAR {year}, IS A LEAP YEAR")
else:
    print(f"THE YEAR {year}, IS NOT A LEAP YEAR")