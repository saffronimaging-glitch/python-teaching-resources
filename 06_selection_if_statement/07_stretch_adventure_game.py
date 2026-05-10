# Stretch Challenge - Adventure Game

print("You enter a dark cave.")

choice = input("Do you go LEFT or RIGHT? ").lower()

if choice == "left":

    print("You find a treasure chest!")

    action = input("Do you OPEN it or LEAVE it? ").lower()

    if action == "open":
        print("You found gold!")

    else:
        print("You leave the treasure behind.")

elif choice == "right":

    print("A dragon appears!")

    action = input("Do you RUN or FIGHT? ").lower()

    if action == "run":
        print("You escaped safely.")

    else:
        print("The dragon defeats you.")

else:
    print("You stand still and nothing happens.")
