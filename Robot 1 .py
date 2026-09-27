# Mon premier robot - Bangangte / Seconde C 2026
# My first robot

for distance in [20, 15, 8, 3, 12]:
    print(f"Je vois un obstacle à {distance}m : ", end="")
    if distance < 10:
        print("Je tourne à droite ! / Turning right!")
    else:
        print("J'avance vite ! / Moving fast!")