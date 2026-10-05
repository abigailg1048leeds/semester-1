# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Please enter a grade between 0 and 100: ")
try: 
    grade = int(grade)
    if grade < 40 and grade >=0:
        print(f"{grade} is a Fail")
    elif grade == 67:
        print("haha six seveeeen")
    elif grade >= 70 and grade <101:
        print (f"{grade} is a Distinction")
    elif grade >= 40 and grade <70:
        print(f"{grade} is a Pass")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")