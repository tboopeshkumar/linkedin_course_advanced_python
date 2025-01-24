cTemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

ftemps1 = [(t*9/5) + 32 for t in cTemps]

ftemps2 ={(t*9/5) + 32 for t in cTemps}

print(ftemps1)
print(ftemps2)

# build a set from an input source

sTemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in sTemp if not c.isspace()}

print(chars)