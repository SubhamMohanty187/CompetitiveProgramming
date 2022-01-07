def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >= 38:
            rem = grades[i] % 5
            if rem >= 3:
                grades[i] = ((grades[i] // 5) + 1) * 5
    return grades
