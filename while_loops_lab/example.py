student_name = input()

fail_counter = 0
grade_counter = 0
years_counter = 0
total_grade = 0

while True:
    current_grade = float(input())
    years_counter += 1
    grade_counter += 1
    total_grade += current_grade

    if current_grade < 4.0:
        fail_counter += 1

    if fail_counter > 1:
        print(f"{student_name} has been excluded at {grade_counter - 1} grade")

    elif years_counter == 12:
        print(f"{student_name} graduated. Average grade: {total_grade / 12:.2f}")

