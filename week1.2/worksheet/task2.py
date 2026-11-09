# Worksheet 1.2: Task 2 Solution
import sys
def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

list = read_numbers()
if len(list) == 0:
    sys.exit("Error: no numbers provided")
max = 0
total = 0
for i in range (len(list)):
    if list[i] > max:

        max = list[i]
    total += list[i]
mean = total/(len(list))
list.sort()
if len(list) % 2 == 1:
    median = list[(len(list)//2)]
else:
    median = ((list[(len(list)//2)-1])+(list[(len(list)//2)]))/2

min = list[0]
print(f"""Minimum = {min}
Maximum = {max}
Median = {median}
Mean = {mean}""")
