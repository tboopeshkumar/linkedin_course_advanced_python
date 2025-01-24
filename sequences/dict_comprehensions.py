ctemps = [0, 12, 34, 100]

tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}

print(tempDict)


# Merge two dictionaries using dictionary comprehension

team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
team3 = { "Hall": 11, "Todd": 22, "Owen": 14}

newTeam = {k:v for team in (team1, team3, team2) for k, v in team.items() }

print(newTeam)