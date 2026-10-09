import math

def cal_paint(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f"You'll need {no_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
cal_paint(test_h, test_w, coverage)