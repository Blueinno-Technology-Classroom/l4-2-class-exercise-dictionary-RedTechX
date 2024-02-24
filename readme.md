# 404B Lesson 4 Class Exercise - Dictionary Manipulations

## Instructions

### Split VS Code Window

You can drag `main.py` tab to the right side of the window to split the window into two panes. This will allow you to see the instructions and the code at the same time.

### Answering

You can answer the questions by writing your answers in the `main.py` file.

You can run the code by clicking the `Run` button on the top right corner of the editor.

The output will be shown in the `Terminal` tab at the bottom of the editor.

## 1. Create a dictionary

```python
empty_dict = {}

student = {
   'name': 'Harry',
   'score': 80,
}
```

## 2. Get value by key

```python
student = {
   'name': 'Harry',
   'score': 80,
}

print(student['name'])   # Harry
print(student['score'])  # 80
print(student['house'])  # Error
```

## 3. Get value in nested dictionary

```python
student = {
   'name': 'Harry',
   'score': {
       'history_of_magic': 80,
       'transfiguration': 79
   }
}

print(student['score']['history_of_magic']) # 80
print(student['score']['transfiguration']) # 79
```

## 4. Add/Edit Value in dictionary

```python
student = {
   'name': 'Harry',
   'score': {
       'history_of_magic': 80,
       'transfiguration': 79
   }
}

student['score']['potion'] = 89  # add
student['score']['history_of_magic'] = 75  # edit
```

## 5. Remove item from dictionary

```python
student = {
   'name': 'Harry',
   'score': {
       'history_of_magic': 80,
       'transfiguration': 79
   }
}

student.pop('name')
student['score'].pop('history_of_magic')

print(student)  # {'score': {'transfiguration': 79}}

```

## 6. Loop through a dictionary

```python
student_scores = {'Harry': 81, 'Ron': 78,
                 'Hermione': 99, 'Draco': 74,
                 'Neville': 62}

for key, val in student_scores.items():
   print(f'key: {key}, value: {val}')

# key: Harry, value: 81
# key: Ron, value: 78
# key: Hermione, value: 99
# key: Draco, value: 74
# key: Neville, value: 62
```

## Questions

1. Print the value of ‘history of magic’ from the dictionary below:

    ```python
   sample_dict = {
       "name": "Hermione",
       "marks": {
           "transfiguration": 90,
           "charms": 98,
           "potions": 98,
           "history of magic": 92,
       }
   }
    ```

2. Update the salary value of employee 3 from 500 to 8500:\
   Initially:

    ```python
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    ```

    Expected:

    ```python
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 8500}
    }
    ```

    > ⚠️ Update the dictionary through code expression, not manually.

3. Print the level of this pokemon when it can learn “curse” from the information below:

   ```python
    mystery_pokemon = {
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
   ```

   Hint:

   ```python
   # Get the list from the dictionary
   move_list = mystery_pokemon['moves']

   # `move_list` stores 3 dictionaries
   # Use the correct index and extract the `level` to learn `curse`
   ```

4. Convert the table below into dictionary in Python:
    | Name      | Score  |
    | ----------| :-------|
    | Harry     | 81     |
    | Ron       | 78     |
    | Hermione  | 99     |
    | Draco     | 74     |
    | Nevill    | 62     |

   ```python
   student_scores = {...}
   ```

5. Following Q4:\
   a. Use a for loop to iterate through the dictionary and print the keys & values.

   b. Find and print the student name with minimum score.

6. Following Q4, write a program to convert scores into grades, then store in a new dictionary.
    | Range      | Description              |
    | ---------- | ------------------------ |
    | Score > 90 | Outstanding              |
    | Score > 80 | Exceeds Expectations     |
    | Score > 70 | Acceptable               |
    | Else       | Fail                     |

   Sample:

   ```python
   student_grades = {
       "Harry": "Exceeds Expectations",
       ...
   }
   ```

7. Merge two lists into a dictionary:

   ```python
    keys = ['Harry', 'Ron', 'Hermione']
    values = ['B', 'C', 'A']
    
    Output:
    {'Harry': 'B', 'Ron': 'C', 'Hermione': 'A'}
   ```

## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
