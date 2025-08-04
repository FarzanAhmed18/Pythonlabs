print("Welcome to the Letter Counter App\n")
name = input("What is your name: ")
print(f"Hello {name}!")
print("I will count the number of times that a specific letter occurs in a message.\n")

message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occurrences of: ")

count = message.lower().count(letter.lower())

if count > 0:
    print(f"\nThe letter '{letter}' appears {count} times in the message.")
else:
    print(f"\nThe letter '{letter}' was not found in the message.")
