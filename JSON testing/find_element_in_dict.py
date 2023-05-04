import json

#Opens, reads and assign the file value to the my_dict variable
with open("Lösen.json", "r") as f:
    my_dict = json.loads(f.read())

length = len(my_dict["passwords"])

#This list will allow the user choose which locations pasword they want
locations = []
i = 0
#Goes trough every dict inside of the password list and assigns the value of the location key to the locations list
for i in range(length):
    print(my_dict["passwords"][i]["location"])
    locations.append(my_dict["passwords"][i]["location"])
    i += 1


i= 0
print("0 Show all")
for i in range(len(locations)):
    print(i + 1, locations[i])
    i += 1

which_location = int(input("Which locations password would you like to see?: "))
if which_location == 0:
    print(my_dict["passwords"])
else:
    which_location += -1

print(my_dict["passwords"][which_location])