import json

my_dict = {
    "passwords": [
        {
            "location": "YouTube",
            "username": "Vapen_Hem1",
            "email": "20",
            "password": "P@ssword1324",
            "notes": "None",
        },
        {
            "location": "Gmail",
            "username": "Vapen_Hem2",
            "email": "20",
            "password": "P@ssword1324",
            "notes": "Backup -> GT",
        },
    ]
}

#LDs = List Dicts, a dict that is inside of a list
#Edit existing LDs
my_dict["passwords"][1] = {"location": "GitHub", "email": "GT", "password": "P@ssword1324", "notes": "None",}

#Add a new LD
new_LD = {"location": "Spotify", "email": "GT", "password": "P@ssword1324", "notes": "None",}
my_dict["passwords"].append(new_LD)

print(my_dict)

"""
{
    "location": "GitHub",
    "email": "GT",
    "password": "P@ssword1324",
    "notes": "None",
},
{
    "location": "Spotify",
    "email": "GT",
    "password": "P@ssword1324",
    "notes": "None",
},
{
    "location": "Microsoft",
    "email": "Far",
    "password": "P@ssword1324",
    "notes": "None",
}
"""
