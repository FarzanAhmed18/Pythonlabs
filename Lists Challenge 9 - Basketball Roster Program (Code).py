import random

print("Welcome the to Basketball Roster Program!")

original_roster = []
 
point_guard = input("Who is your point guard:")
shooting_guard = input("Who is your shooting guard:")
small_forward = input("Who is your small forward:")
power_forward = input("Who is your power forward:")
center = input("Who is your center:")

original_roster.append(point_guard)
original_roster.append(shooting_guard)
original_roster.append(small_forward)
original_roster.append(power_forward)
original_roster.append(center)

roster = {
    "Point Guard": point_guard,
    "Shooting Guard": shooting_guard,
    "Small Forward": small_forward,
    "Power Forward": power_forward,
    "Center": center
}

print(f"Your starting 5 for the upcoming basketball season\n Point Guard: {point_guard}\n Shooting Guard: {shooting_guard}\n Small Forward: {small_forward}\n Power Forward: {power_forward}\n Center: {center}")

injured_position = random.choice(list(roster.keys()))
injured_player = roster[injured_position]
del roster[injured_position]

print(f"\n Oh no! {injured_player}, has been injured!\n There are only 4 players on the roster.")
new_player = input(f"Who will take {injured_player}'s spot:\n")

roster[injured_position] = new_player

print("Your starting 5 for the upcoming basketball season")
for position, player in roster.items():
    print(f"{position}: {player}")
