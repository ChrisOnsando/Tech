thisismylistofteams = ["Manchester United" ,"Manchester City", "Bayern Munich", "PSG", "Liverpool", "Real Madrid", "Athletico Madrid", "Juventus", "Inter Milan", "AC Milan", "Arsenal" ,"Best teams to support", "In the football leagues" ]
thisismyotherteams = ["Chelsea", "Westham", "Borrusia Dortmund"]
thisismylistofteams.extend(thisismyotherteams)
print(thisismylistofteams)
print(len(thisismylistofteams))
print(type(thisismylistofteams))
print(thisismylistofteams[2])
print(thisismylistofteams[-1])
print(thisismylistofteams[0])
print(thisismylistofteams[2:5])
print(thisismylistofteams[:5])


thisismylistofteams.reverse()
print(thisismylistofteams)

for x in thisismylistofteams:
    print(x)

[print(x) for x in thisismylistofteams]

if "Manchester City" in thisismylistofteams:
 print("Yes", "It is in my favourite teams list")
else:
     print("Not in my favourite teams list", thisismylistofteams)

     mylist = thisismylistofteams.copy()
     print(mylist)