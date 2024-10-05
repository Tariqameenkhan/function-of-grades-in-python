# Collecting subjects and marks as lists
subject_names = []
subject_marks = []

for i in range(4):
    subject = input(f"Enter subject {i + 1} name: ")
    marks = int(input(f"Enter subject {i + 1} marks obtained out of 100: "))
    
    if marks < 0 or marks > 100:
        print("Error: Marks should be between 0 and 100.")
        break
    else:
        subject_names.append(subject)
        subject_marks.append(marks)

# Ensure the loop only runs if all inputs are valid
if len(subject_marks) == 4:
    total_marks = sum(subject_marks)
    percentage = (total_marks / 400) * 100

    # Determine the grade based on percentage
    if percentage >= 90:
        grade = "A"
        result = "Pass"
    elif percentage >= 80:
        grade = "B"
        result = "Pass"
    elif percentage >= 70:
        grade = "C"
        result = "Pass"
    elif percentage >= 60:
        grade = "D"
        result = "Pass"
    else:
        grade = "F"
        result = "Fail"

    # Output the results
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print(f"Total Marks: {total_marks}/400")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Subjects: {subject_names}")
    print(f"Marks: {subject_marks}")
