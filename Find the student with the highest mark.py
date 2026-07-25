students = {
    "Ram": 85,
    "Arun": 90,
    "Sam": 78,
    "Hari": 88
}

Top_student = ""
highest_mark = 0

for key in students:
    if students[key] > highest_mark:
        highest_mark = students[key]
        Top_student = key

print("Top Student =", Top_student)
print("Highest Mark =", highest_mark)