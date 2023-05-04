import json

#Json Struktur
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
        {
            "location": "GitHub",
            "username": "Vapen_Hem3",
            "email": "GT",
            "password": "P@ssword1324",
            "notes": "None",
        },
        {
            "location": "Spotify",
            "username": "Vapen_Hem4",
            "email": "GT",
            "password": "P@ssword1324",
            "notes": "None",
        },
        {
            "location": "Microsoft",
            "username": "Vapen_Hem5",
            "email": "Far",
            "password": "P@ssword1324",
            "notes": "None",
        }
    ]
}

#Skriver till Lösen filen
json_string = json.dumps(my_dict)
with open("Lösen.json", "w") as f:
    f.write(json_string)