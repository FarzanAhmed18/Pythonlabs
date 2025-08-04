import random

print("Welcome to the Basketball Roster Program!")

# Collect player inputs
point_guard = input("Who is your Point Guard? ")
shooting_guard = input("Who is your Shooting Guard? ")
small_forward = input("Who is your Small Forward? ")
power_forward = input("Who is your Power Forward? ")
center = input("Who is your Center? ")

# Create a dictionary to store players by position
roster = {
    "Point Guard": point_guard,
    "Shooting Guard": shooting_guard,
    "Small Forward": small_forward,
    "Power Forward": power_forward,
    "Center": center
}

# Display the original lineup
print("\n Your Starting 5 for the Upcoming Season:")
for position, player in roster.items():
    print(f"{position}: {player}")

# Choose a random player to simulate an injury
injured_position = random.choice(list(roster.keys()))
injured_player = roster[injured_position]
del roster[injured_position]

# Notify about the injury and ask for replacement
print(f"\n Oh no! {injured_player}, your {injured_position}, has been injured!")
new_player = input(f"Who will replace {injured_player} as {injured_position}? ")

# Add replacement to the roster
roster[injured_position] = new_player

# Display the updated lineup
print("\n Updated Starting 5:")
for position, player in roster.items():
    print(f"{position}: {player}")
