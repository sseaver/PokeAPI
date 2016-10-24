import requests


def get_all_cards():
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards",
                          headers={
                            "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV"
                          }
                          )

    json_result = result.json()
    for card in json_result:
        try:
            print("""
            Name: {}
            Cardset: {}
            Cost: {}
            Attack: {}
            Health: {}
            Rarity: {}
            Text: {}
            """.format(card['name'], card['cardSet'], card['cost'], card['attack'],
                       card['health'], card['rarity'], card['text']))
        except:
            print("Sorry, one of these attributes is unavailable")


def get_cards_by_name(name):
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}/".format(name),
                          headers={
        "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV"
      }
    )

    json_result = result.json()

    print("""
    Name: {}
    Cardset: {}
    Cost: {}
    Attack: {}
    Health: {}
    Rarity: {}
    Text: {}
    """.format(json_result[0].get('name'), json_result[0].get('cardSet'), json_result[0].get('cost'),
               json_result[0].get('attack'), json_result[0].get('health'), json_result[0].get('rarity'),
               json_result[0].get('text')))


def get_cards_by_class(class_name):
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/classes/{}".format(class_name),
                          headers={
                          "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV"
                          }
                          )

    json_result = result.json()
    for card in json_result:

        print("""
        Name: {}
        Cardset: {}
        Type: {}
        Text: {}
        """.format(card['name'], card['cardSet'], card['type'], card['text']))


def list_cardSet(value):
    # Sean helped alot with this fuction
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/info",
                          headers={
                            "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV",
                            "Accept": "application/json"
                            }
                          )

    json_result = result.json()

    for card in json_result[value]:
        print(card)


def get_cards_by_cardSet(set_name):
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/{}".format(set_name),
                          headers={
                          "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV"
                          }
                          )

    json_result = result.json()

    for card in json_result:
        try:
            print("""
            Name: {}
            Type: {}
            Text: {}
            """.format(card['name'], card['type'], card['text']))
        except:
            print("Sorry, one of these attributes is unavailable")


def get_cards_by_race(race_name):
    result = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/races/{}".format(race_name),
                          headers={
                          "X-Mashape-Key": "dYF93xiQJTmsh4vRLYxc1NJg01wnp1GE6YTjsnXfWTO46owudV"
                          }
                          )

    json_result = result.json()

    for card in json_result:
        try:
            print("""
            Name: {}
            Cardset: {}
            Cost: {}
            Attack: {}
            Health: {}
            Rarity: {}
            Text: {}
            """.format(card['name'], card['cardSet'], card['cost'], card['attack'], card['health'], card['rarity'],
                       card['text']))
        except:
            print("Sorry, one of these attributes is unavailable")


while True:
    response = input("""Would you like to view by:
    1: Name
    2: Class
    3: CardSet
    4: Race
    5: All Card sets
    6: All Classes
    7: All Races
    """)
    if response == "1":
        name = input("What is the name you would like to view?")
        get_cards_by_name(name)
    elif response == "2":
        class_name = input("What is the name of the class you would like to view?")
        get_cards_by_class(class_name)
    elif response == "3":
        set_name = input("Which cardSet would you like to view?")
        get_cards_by_cardSet(set_name)
    elif response == "4":
        race_name = input("Which race would you like to view?")
        get_cards_by_race(race_name)
    elif response == "5":
        list_cardSet('sets')
    elif response == "6":
        list_cardSet('classes')
    elif response == "7":
        list_cardSet('races')
    # elif response == "5":
    #     get_all_cards()

    exit = input("Press enter to continue, type 'n' to exit")

    if not exit == "":
        break
