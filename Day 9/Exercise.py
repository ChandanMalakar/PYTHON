travel_log=[
    {
    "country":"France",
    "cities_visited" : ["Paris","Dijon"],
    "total_visits":12
    },
    {
    "country":"Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits" : 5
    },
]

# PROCESS OF THE PROGRAM 
def add_new_country(country,number_of_visits,cities_visited):
    add_country={}
    add_country["country"]=country
    add_country["cities_visited"]=cities_visited
    add_country["total_visits"]=number_of_visits
    travel_log.append(add_country)



# END OF PROGRAM

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

length=len(travel_log)
for i in range(0,length):
    if i==2:
        print(f"You've visited {travel_log[i]["country"]} {travel_log[i]["total_visits"]} times.")
        print(f"You've been to {travel_log[i]["cities_visited"][0]} and {travel_log[i]["cities_visited"][1]}.")