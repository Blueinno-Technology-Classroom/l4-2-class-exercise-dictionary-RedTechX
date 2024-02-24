##################################################
'''
Q1: 
'''
hermione_portfolio = {
   "name": "Hermione",
   "marks": {
       "transfiguration": 90,
       "charms": 98,
       "potions": 98,
       "history of magic": 92,
   }
}

print(hermione_portfolio["marks"]['history of magic'])
print()
##################################################
'''
Q2:
'''

# TODO: Write your code here

moneymoney = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

moneymoney['emp3']['salary'] = 8500
print(moneymoney['emp3']['salary'])
print()
##################################################
'''
Q3:
'''

# TODO: Write your code here
mopeckey = {
    "height": 15,
    "weight": 405,
    "moves": [
        {
            "name": "lick",
            "level_learned_at": 0
        },
        {
            "name": "nightmare",
            "level_learned_at": 0
        },
        {
            "name": "curse",
            "level_learned_at": 16
        }
    ]
}

for move in mopeckey['moves']:
    if move['name'] == 'curse':
        print(move['level_learned_at'])

print()
##################################################
'''
Q4:
'''

# TODO: Write your code here

student_scores = {
    'Harry' : 81,
    'Ron' : 78,
    'Hermione' : 99,
    'Draco' : 74,
    'Nevill' : 62
}

print(student_scores)
print()
##################################################
'''
Q5a:
'''

# TODO: Write your code here

def print_dict(d):
    for k in d:
        print(f'{k}:  {d[k]}')
    print()

print_dict(student_scores)
##################################################
'''
Q5b:
'''
min_score = 100
min_student = ''

# TODO: Write your code here
for s in student_scores:
    if student_scores[s] < min_score:
        min_score = student_scores[s]
        min_student = s

print(min_student)
##################################################
'''
Q6:
'''

# TODO: Write your code here


def give_grade(score: int) -> str:
    grade = 'Fail'
    if score > 90:
        grade = 'Outstanding'
    elif score > 80:
        grade = 'Exeeds Expectations'
    elif score > 70:
        grade = 'Acceptable'
    
    return grade

print()
print_dict({s : give_grade(student_scores[s]) for s in student_scores})
##################################################
'''
Q7:
'''
keys = ['Harry', 'Ron', 'Hermione']
values = ['B+', 'C-', 'A++']



# TODO: Write your code here

# student_marks = {}
# for i in range(len(keys)):
#     k = keys[i]
#     v = values[i]
#     student_marks[k] = v

student_marks = {k : v for k, v in zip(keys, values)}

print_dict(student_marks)
##################################################
