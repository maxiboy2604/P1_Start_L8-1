import random

voorvoegsel = ["super","skibidi","obese","bikestealing","amazing","bleuberry"]
achtervoegsel = ["mootje","daan","rune","lennert"]

for i in range (10):
    gekozen_voorvoegsel = random.choice(voorvoegsel)
    gekozen_achtervoegsel = random.choice(achtervoegsel)
    print("De random naam is: " + gekozen_voorvoegsel, gekozen_achtervoegsel)
    kleur = random.choice(kleuren)
    for i in range(30):