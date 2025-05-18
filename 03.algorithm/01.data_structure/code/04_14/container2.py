### remove ()
sport=['축구', '농구', '배구', '야구',"야구"]
print(f"sport : {sport}")
print(f"길이 : {len(sport)}")

while '야구' in sport:
    sport.remove('야구')

print(f"sport : {sport}")
print(f"길이 : {len(sport)}")
