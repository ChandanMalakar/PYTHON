# # import turtle
# from turtle import Turtle, Screen
#
# # timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse", "black")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
pokemon = PrettyTable()
table.add_column("Name",["Chandan","Madhav","Sawan","Dilip"])
table.add_column("Dept",["CSE","CSE","CSE","CIVIL"])
table.add_column("RegNo",[526,556,536,503])
table.add_column("State",["Jharkhand","Bihar","Campbel Bay","Campbel Bay"])
print(table)

pokemon.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
pokemon.add_column("Type",["Electric","Water","Fire"])
pokemon.align = "c"
print(pokemon)

