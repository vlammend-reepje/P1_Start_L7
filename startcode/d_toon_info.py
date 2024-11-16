persoonsdata = {
	"Naam": "John",
	"Leeftijd": "25",
	"Favoriete kleur": "blauw"
}

persoonsdata ["hobby"] = "codefever"

print(persoonsdata["hobby"])
print(persoonsdata["Favoriete kleur"])


print(persoonsdata['Naam'] + " is " + persoonsdata['Leeftijd'] + " jaar.")

print(f"{persoonsdata['Naam']} is {persoonsdata['Leeftijd']} jaar")