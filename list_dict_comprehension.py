import random

numbers = [1,2,3]
new_list = []

for n in numbers:
    sum = n + 1
    new_list.append(sum)

print(new_list)

newer_list = [number + 1 for number in numbers]
#newer_list = [new_item for item in list if test]


names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

students_scores = {name:random.randint(1,100) for name in names}
#students_scores = {key:value for item in list}
print(students_scores)

passed_students = {name:students_scores[name] for name in students_scores if students_scores[name] > 60}
print(passed_students)

another_passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
#another_passed_students = {new_key:new_value for (key,value) in old_dictionary if test}
print(another_passed_students)