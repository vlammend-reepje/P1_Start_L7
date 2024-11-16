prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")

antwoord = int(input (""))

def herhalen():
    if antwoord == 1:
        print (prijzenkast [0])
        herhalen()
    elif antwoord == 2:
        print (prijzenkast [1])
        herhalen()
    elif antwoord == 3:
        print (prijzenkast [2])
        herhalen()