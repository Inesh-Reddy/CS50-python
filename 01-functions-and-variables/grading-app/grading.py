# Accepts numerical scores as input.
# Converts scores to standard letter grades (e.g., A, B, C, D, F).
# Customizable grading thresholds (e.g., an "A" might be 90–100, "B" might be 80–89).
# Outputs a user-friendly summary of results.
# Run the program and follow the prompts to input scores.
    # Example Input:
    # Enter scores (comma-separated): 95, 82, 73, 60, 45

    # Example Output:
    # Score 95: A
    # Score 82: B
    # Score 73: C
    # Score 60: D
    # Score 45: F
# 



val = input("Please input values separated by a comma: ")

gradesList = []


values = val.split(",")
print(values);
for i in range(len(values)):
    gradesList.append(int(values[i].strip())) 

print(gradesList);

for grade in gradesList:
    if grade >= 90:
        print(f"Score {grade}: A")
    elif grade >= 80:
        print(f"Score {grade}: B")
    elif grade >= 70:
        print(f"Score {grade}: C")
    elif grade >= 60:
        print(f"Score {grade}: D")
    else:
        print(f"Score {grade}: F")
