# --- Section 1: Define the Lists ---
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# --- Section 2: Print Summary Table ---
print("Summary Table\n")

# Function to print summary of a list
def print_summary(name, lst):
    print(f"The variable {name} is a {type(lst)}.")
    print(f"It contains the elements: {lst}")
    print(f"The element {lst[0]} is a {type(lst[0])}.\n")

print_summary("num_strings", num_strings)
print_summary("num_ints", num_ints)
print_summary("num_floats", num_floats)
print_summary("num_lists", num_lists)

# --- Section 3: Sorting and Comparison ---
print("Now sorting num_strings and num_ints...")

# Sort the lists permanently
num_strings.sort()
num_ints.sort()

# Print sorted lists
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")

# --- Section 4: Explanation ---
# Strings are sorted alphabetically (lexicographically), not numerically
print("Strings are sorted alphabetically while integers are sorted numerically!")
