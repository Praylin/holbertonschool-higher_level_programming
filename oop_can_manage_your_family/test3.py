from family import Person, Baby, Teenager, Adult, Senior

Tony = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
Tony.last_name = "Foto"
print Tony.json()

Tony_json = {'last_name': "Foto", 'first_name': "Tony", 'genre': "Male", 'date_of_birth': [7, 4, 2015], 'eyes_color': "Brown", 'ide': 3}
Tony.load_from_json(Tony_json)
print Tony.last_name
