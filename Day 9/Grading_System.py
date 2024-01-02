student_scores={
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades={}
for scores in student_scores:
    if student_scores[scores]>90:
        student_grades[scores]="Outstanding"
    elif student_scores[scores]>80:
        student_grades[scores]="Exceeds Expectations"
    elif student_scores[scores]>70:
        student_grades[scores]="Acceptable"
    else:
        student_grades[scores]="Fail"
print(student_grades)
