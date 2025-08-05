import random
import math

print("---- Powerball Simulator ----\n")

# Phase 1: Get game settings with input validation
while True:
    white_input = input("How many White Balls to draw 5 balls from? (Usually 69): ")
    if white_input.isdigit():
        white_balls = int(white_input)
        if white_balls < 5:
            print("Please pick at least 5 White Balls to draw from.")
        else:
            break
    else:
        print("Please enter a whole number.")

while True:
    red_input = input("How many Red Balls to draw 1 ball from? (Usually 26): ")
    if red_input.isdigit():
        red_balls = int(red_input)
        if red_balls < 1:
            print("Please pick at least 1 Red Ball to draw from.")
        else:
            break
    else:
        print("Please enter a whole number.")

# Calculate odds
odds = math.comb(white_balls, 5) * red_balls
odds_percentage = f"{(1 / odds) * 100:.8f}%"
print(f"\nYou have a 1 in {odds:,} chance of winning, or about {odds_percentage}")

# Phase 2: Generate winning numbers
winning_white = sorted(random.sample(range(1, white_balls + 1), 5))
winning_red = random.randint(1, red_balls)
winning_numbers = winning_white + [winning_red]

print("\n---------Welcome to the Power-Ball-----------")
print("Tonight's winning numbers are: ", end='')
print(*winning_numbers)
input("Press 'Enter' to begin purchasing tickets!!!\n")

# Phase 5 & 6: Ticket purchasing loop
tickets_sold = []
total_tickets = 0
active = True

while active:
    # Ask how many tickets to buy in this round
    while True:
        interval_input = input("How many tickets would you like to purchase in this interval? ")
        if interval_input.isdigit() and int(interval_input) > 0:
            ticket_interval = int(interval_input)
            break
        else:
            print("Please enter a positive whole number.")

    # Generate tickets for this interval
    new_tickets = []
    for _ in range(ticket_interval):
        white_numbers = sorted(random.sample(range(1, white_balls + 1), 5))
        red_number = random.randint(1, red_balls)
        ticket = white_numbers + [red_number]

        # Check if ticket already bought
        if ticket not in tickets_sold:
            tickets_sold.append(ticket)
            total_tickets += 1
            print(ticket)
            # Check if this ticket is the winner
            if ticket == winning_numbers:
                print(f"\nWinning ticket numbers: {' '.join(map(str, ticket))}")
                print(f"Purchased a total of {total_tickets} tickets.")
                active = False
                break
        else:
            print("Losing ticket generated; disregard...")

    if not active:
        break

    # After the interval, show total tickets purchased
    print(f"\n{total_tickets} tickets purchased so far with no winners...")

    # Ask user if they want to keep buying
    while True:
        keep_going = input("Keep purchasing tickets (y/n): ").lower()
        if keep_going in ['y', 'n']:
            break
        else:
            print("Please enter 'y' or 'n'.")

    if keep_going == 'n':
        active = False

if active == False and total_tickets != 0 and ticket != winning_numbers:
    print(f"\nYou bought {total_tickets} tickets and still lost!")
    print("Better luck next time!")
