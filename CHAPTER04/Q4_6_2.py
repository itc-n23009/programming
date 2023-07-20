students_by_height = sorted(students_data, key=lambda s: s[1])
students_by_weight = sorted(students_data, key=lambda s: s[2])
print("\nSort by height")
for student in students_by_height:
    print(student)
