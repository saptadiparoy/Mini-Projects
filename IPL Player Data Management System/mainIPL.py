import IPLmanager as manager
from player import Player


while True:
    print ("List of actions:")
    print ("1.Add Player \n2.Delete Player \n3.Update Player \n4.View Players \n5.Save Json File \n0.Exit")

    choice = int(input("Enter Choice    :   "))

    try:

        if choice == 1:
            num = int(input("enter num    :"))
            name = input("enter name    :")
            age = int(input("enter age    :"))
            team = input("enter team    :")

            manager.add(num, name, age, team)

        elif choice == 2:
            num = int(input("Enter player num   :   "))
            manager.remove(num)

        elif choice == 3:
            num = int(input("Enter Num of Player to Update  :   "))
            name = input("enter name    :")
            age = int(input("enter age    :"))
            team = input("enter team    :")
            manager.update(num, name, age, team)

        elif choice == 4:
            manager.view()

        elif choice == 5:
            manager.savejson()

        elif choice == 0:
            print("Goodbye!!")
            break

        else:
            print ("Invalid Input!!")


    except Exception as e:
        print(f"Could not Run due to {e}")
