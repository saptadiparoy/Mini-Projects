from player import Player
import json

PLAYERS = []

def add(num, name, age, team):
    ply = Player(num, name, age, team)
    PLAYERS.append(ply)
    print ("Added Player    :   ", ply)

def remove(num):
    for p in PLAYERS:
        if p.num == num:
            PLAYERS.remove(p)
            print (f"Player Removed.")

    print ("Player not found.")

def update(num, name, age, team):
    for p in PLAYERS:
        if p.num == num:
            p.name = name
            p.age = age
            p.team = team

            print("Player updated   :  ", p)

        else :
            print ("Player Not Found.")

    
def view():
    print ("Viewing all players:")
    for p in PLAYERS:
        print(p.display())

def savejson():
    try:
        f = open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\SEM2\\IPL Player Management System\\playerdata.json", "w", newline="")
        json.dump([p.to_dict() for p in PLAYERS], f, indent=2)
        print(f"Data saved.")
    except (OSError, IOError) as e:
        print(f"Could not save data due to: {e}")

