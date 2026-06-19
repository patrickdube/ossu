def find_grades(grades, students):
    grades_list = []
    for student in students:
        grades_list.append(grades[student])
    return grades_list

# d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy']))

def find_in_L(Ld, k):
    for d in Ld:
        if k in d:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))
print(find_in_L([d1, d2, d3], 25))
