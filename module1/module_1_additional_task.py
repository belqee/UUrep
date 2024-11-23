grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
averages = [sum(student_grades) / len(student_grades) for student_grades in grades]
dictionary = dict(zip(students, averages))
print(dictionary)