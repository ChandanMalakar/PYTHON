# THIS PROGRAM IS TO CALCULATE THE TOTAL COST OF THE CANS OF PAINT REQUIRED TO PAINT THE GIVEN SURFACE AREA OF WALL

def paint_calc(height,width,cover):
    number_of_cans=((height*width)/cover)
    number_of_cans=round(number_of_cans)
    print(f"To paint the given wall, a total of {number_of_cans} cans are required.")




test_h=int(input("Height of the wall : "))
test_w=int(input("Width of the wall : "))
coverage=5
paint_calc(height=test_h, width=test_w, cover=coverage) 

# TO ROUND UP A NUMBER, YOU CAN DO IT BY TWO METHODS :
# 1ST USING round() FUNCTION OF PYTHON
# 2ND USING (#import math) then (math.ceil() / math.floor() )