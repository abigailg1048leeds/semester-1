import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
    num = int(input("Enter a number of names: "))
    chosen = [-1]
    x = -1
    for i in range (num):
        while x in chosen:
            x= random.randint(0,len(names)-1)
        chosen.append(x)
        print(names[x])


# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
