import random

response = "n"

while response == "n":
    response = input("Do you want to roll a dice? (y/n) ")
number = random.randint(1,6)
if number == 1:
    print("[-----]")
    print("       ")
    print("   o   ")
    print("       ")
    print("[-----]")
elif number == 2:
    print("[-----]")
    print("     o ")
    print("       ")
    print(" o     ")
    print("[-----]")
elif number == 3:
    print("[-----]")
    print("     o ")
    print("   o   ")
    print(" o     ")
    print("[-----]")
elif number == 4:
    print("[-----]")
    print(" o   o ")
    print("       ")
    print(" o   o ")
    print("[-----]")
elif number == 5:
    print("[-----]")
    print(" o   o ")
    print("   o   ")
    print(" o   o ")
    print("[-----]")
elif number == 6:
    print("[-----]")
    print(" o o o ")
    print("       ")
    print(" o o o ")
    print("[-----]")