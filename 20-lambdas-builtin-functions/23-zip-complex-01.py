# zip() complex examples

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

print(f"midterms: {midterms}")
print(f"finals: {finals}")
print(f"students: {students}")

# Get the highest grade from midterms and finals using list comprehension
print("\nUsing list comprehension ot get the highest grade:")
print("Statement: [max(grades) for grades in zip(midterms, finals)]")
final_grades = [max(grades) for grades in zip(midterms, finals)]
print(final_grades)

# Create a dictionary of students and their highest grade using dictionary comprehension
print("\nUsing dictionary comprehension to get student name & highest grade:")
print("Statement: {grades[0]: max(grades[1], grades[2]) for grades in zip(students, midterms, finals)}")
final_grades_dict = {grades[0]: max(grades[1], grades[2]) for grades in zip(students, midterms, finals)}
print(final_grades_dict)

# Get the student and highest score using lanbda, map() and zip()
print("\nUsing lambda, map() & zip() to get student name & highest grade:")
print("Statement: dict(zip(students, map(lambda grade: max(grade), zip(midterms, finals))))")
scores = zip(students,
             map(lambda grade: max(grade), zip(midterms, finals))
             )
print(f"Scores: {dict(scores)}")

print("\nGet average grades using lambda, map() & zip():")
print("Statement: dict(zip(students, map(lambda grade: ((grade[0] + grade[1]) / 2), zip(midterms, finals))))")
average_scores = zip(students,
                     map(lambda grade: ((grade[0] + grade[1]) / 2), zip(midterms, finals))
                     )
print(f"Average grades: {dict(average_scores)}")
