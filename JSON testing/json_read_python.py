import json

with open("Lösen.json", "r") as f:
    json_var = json.loads(f.read())

print(json_var)
#Prints the location value from the third Dict in the passwords list
print(json_var["passwords"][2]["location"])
#Prints the username value from the third Dict in the passwords list
print(json_var["passwords"][2]["username"])
#Prints the email value from the third Dict in the passwords list
print(json_var["passwords"][2]["email"])
#Prints the password value from the third Dict in the passwords list
print(json_var["passwords"][2]["password"])
#Prints the notes value from the third Dict in the passwords list
print(json_var["passwords"][2]["notes"])