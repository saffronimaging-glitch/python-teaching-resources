# Nested Selection - Robot Chef

has_bread = True
has_butter = True
has_jam = False

if has_bread:

    print("Bread available.")

    if has_butter:
        print("Butter added.")

        if has_jam:
            print("Jam added.")
            print("Jam sandwich complete!")

        else:
            print("No jam available.")

    else:
        print("No butter available.")

else:
    print("No bread available.")
