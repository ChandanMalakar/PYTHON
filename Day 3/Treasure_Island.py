#WELCOME TO THE TREASURE ISLAND
print(''' _____                                    ___     _                 _ 
|_   _| __ ___  __ _ ___ _   _ _ __ ___  |_ _|___| | __ _ _ __   __| |
  | || '__/ _ \/ _` / __| | | | '__/ _ \  | |/ __| |/ _` | '_ \ / _` |
  | || | |  __/ (_| \__ \ |_| | | |  __/  | |\__ \ | (_| | | | | (_| |
  |_||_|  \___|\__,_|___/\__,_|_|  \___| |___|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure. ")
direction=input("Do you want to take Left or Right : ")
if direction=="Left":
	print("There is a lake nearby...")
	swim=input("Do you want to swim or wait : ")
	if swim=="wait":
		print("You've escaped the danger successfully..")
		print("There are 3 doors infront of you...")
		door=input("Which door do you want to take : Red, Yellow, or Blue : ")
		if door=="Red":
			print("Game Over.")
		elif door=="Yellow":
			print("You Win!.")
		else:
			print("Game Over.")
	else:
		print("Game Over.")
else:
	print("Game Over.")
