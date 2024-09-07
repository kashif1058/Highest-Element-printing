student_scores = input("Enter your list of scores: \n").split()

# Debug print to show the list of scores as strings
print(student_scores)

# Convert all string elements in the list to integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the variable to store the highest score
highest_score = 0

# Loop through each score in the list to find the highest one
for score in student_scores:
    if score >= highest_score:
        highest_score = score

# Print the highest score
print(f"The highest score is : {highest_score}")

student_scores = input("Enter your list of scores: \n").split()

# Debug print to show the list of scores as strings
print(student_scores)

# Convert all string elements in the list to integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the variable to store the highest score and a count
highest_score = 0
occurrences = 0

# Loop through each score in the list to find the highest one
for score in student_scores:
    if score > highest_score:
        highest_score = score
        occurrences = 1
    elif score == highest_score:
        occurrences += 1
        print(f"The score {score} appears again as the highest score.")

# Print the highest score
print(f"The highest score is: {highest_score}")

# Print how many times the highest score appears
if occurrences > 1:
    print(f"The highest score {highest_score} appears {occurrences} times.")
else:
    print(f"The highest score {highest_score} appears only once.")

Prompt the user to input a list of scores
student_scores = input("Enter your list of scores: \n").split()

# Debug print to show the list of scores as strings
print(student_scores)

# Convert all string elements in the list to integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the variable to store the highest score
highest_score = 0
highest_score_found = False

# Loop through each score in the list to find the highest one
for score in student_scores:
    if score > highest_score:
        highest_score = score
        highest_score_found = False  # Reset the flag when a new highest score is found
    elif score == highest_score and not highest_score_found:
        highest_score_found = True
        print(f"The score {score} appears again as the highest score.")

# Print the highest score