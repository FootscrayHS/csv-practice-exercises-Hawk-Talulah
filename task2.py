# Task 2 — Filter by City
# Read students.csv and display only students from a given city.
any_students = False
students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

city_to_find = input('Enter a city: ')

# Your code below — find all students from that city
print("students from " + city_to_find + ":")
for i in students:
    if i[2].lower() == city_to_find.lower():
        print(i[0] + " (age " + i[1] + ")")
        any_students = True
if any_students == False:
    print("No one in that city")