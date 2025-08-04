print("Welcome to the Grade Sorter App")

# Grades Input
first_grade = float(input("What is your first grade (0-100): "))
second_grade = float(input("What is your second grade (0-100): "))
third_grade = float(input("What is your third grade (0-100): "))
fourth_grade = float(input("What is your fourth grade (0-100): "))

# Creating First list (grades)
grades = [first_grade, second_grade, third_grade, fourth_grade]

# Formatting grades
formatted_grades = [f"{num:.6g}" for num in grades]

# Printing Grades
print("\nYour grades:", formatted_grades)

# Sorted Grades from highest to lowest
grades.sort(reverse=True)
formatted_grades2 = [f"{num:.6g}" for num in grades]
print("\nYour grades from highest to lowest:")
print(formatted_grades2)

# Drop the two lowest grades
print("\nThe lowest two grades will now be dropped.")
removed_grades = sorted(grades[-2:])  # lowest two, sorted ascending
formatted_removed_grades = [f"{num:.6g}" for num in removed_grades]
print("Removed grades:\n", formatted_removed_grades)

# Highest two grades
high_grades = grades[:2]
formatted_high_grades = [f"{num:.6g}" for num in high_grades]
print("\nYour remaining grades are:", formatted_high_grades)

# Get the highest grade
highest_grade = high_grades[0]
print(f"\nNice work! Your highest grade is a {highest_grade:g}")
