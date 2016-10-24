import requests


def get_firstgen_pokemon():
    url = "http://pokeapi.co/api/v2/pokemon/"

    result = requests.get(url)

    json_result = result.json()
    print(json_result)
    for pokemon in json_result:
        print("""
        Name: {}
        Number(ID): {}
        Type: {}
        Moves: {}
        Species: {}
        Weight: {}
        Height: {}
        """.format(pokemon['name'], pokemon['id'], pokemon['types'], pokemon['moves'], pokemon['species'],
                   pokemon['weight'], pokemon['height']))


def get_pokemon_by_name(name):
    url = "http://pokeapi.co/api/v2/pokemon/{}/".format(name)

    result = requests.get(url)

    json_result = result.json()

    for pokemon in json_result:
        print("""
        Name: {}
        Number(ID): {}
        Type: {}
        Moves: {}
        Species: {}
        Weight: {}
        Height: {}
        """.format(pokemon['name'], pokemon['id'], pokemon['types'], pokemon['moves'], pokemon['species'],
                   pokemon['weight'], pokemon['height']))


def get_game(id_number):
    url = "http://pokeapi.co/api/v2/generation/{}".format(id_number)

    result = requests.get(url)

    json_result = result.json()

    print("""
    Name: {}
    ID: {}
    Main Region: {}
    Pokemon Species: {}
    Other Names, Language: {}, {}
    """.format(json_result[0]['name'], json_result[0]['id'], json_result[0]['main_region'],
               json_result[0]['pokemon_species'], json_result[0]['names']))


def list_games():
    url = "http://pokeapi.co/api/v2/generation"

    result = requests.get(url)

    json_result = result.json()

    for game in json_result:
        print("""
        Name: {}
        """.format(game['name']))


def list_items():
    url = "http://pokeapi.co/api.v2/item"

    result = requests.get(url)

    json_result = result.json()

    for item in json_result:
        print("""
        Name: {}
        """.format(item['name']))


def get_item(name):
    url = "http://pokeapi.co/api.v2/item/{}".format(name)

    result = requests.get(url)

    json_result = result.json()

    print("""
    Name: {}
    Cost: {}
    Attributes: {}
    """.format(json_result[0]['name'], json_result[0]['cost'], json_result[0]['attributes']))


while True:
    response = input("""What would you like to view?
    1: All First Generation pokemon
    2: Search Pokemon by name
    3: List of all games
    4: Search games by id
    5: List of all items
    6: Search items by name
    \n""")

    if response == "1":
        get_firstgen_pokemon()
    elif response == "2":
        name = input("What is the name of the Pokemon you want to view? \n")
        get_pokemon_by_name(name)
    elif response == "3":
        list_games()
    elif response == "4":
        id_number = input("What is the id for the game you want to view?\n")
        get_game(id_number)
    elif response == "5":
        list_items()
    elif response == "6":
        name = input("What is the name of the item you want to view?\n")
        get_item(name)

    exit = input("Press enter to continue, type 'n' to exit")

    if not exit == "":
        break
