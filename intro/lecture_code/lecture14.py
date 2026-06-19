def find_grades(grades, students):
    grades_list = []
    for student in students:
        grades_list.append(grades[student])
    return grades_list

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy']))
