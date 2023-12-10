age=int(input("What is your current age? "))

remaining_age=90-age

months=remaining_age*12
weeks=52*remaining_age
days=365*remaining_age

message_of_devil=f"You have {days} days, {weeks} weeks and {months} months left"
print(message_of_devil)