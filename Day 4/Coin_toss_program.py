import random

print("WELCOME TO COIN TOSS PROGRAM")
Heads=0
Tails=1
random_side=random.randint(0,1)
if random_side==0:
    print("Heads")
else:
    print("Tails")