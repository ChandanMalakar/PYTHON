# year=int(input("Enter a year:"))


def is_leap(year):
    """this function determines if the given year is a leap year or not""" #THIS PART IS KNOWN AS "DOCSTRING"
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(yr,mon):
    """this function calculates and returns the number of days in a month given by the user"""
    if mon>12 or mon<1:
        return "Invalid Month"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    # if yr%4==0 or yr%100==0 and yr%400==0:
    if is_leap(yr) and mon==2:
        # if mon==2:
        #     month_days[2-1]=29
        return 29
    return month_days[mon-1]


year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
days=days_in_month(year,month)
print(days)