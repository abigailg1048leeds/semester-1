import random

# Get user to input how many random numbers they want

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
num = int(input("Enter a number of random numbers: "))
for i in range(num):
    with open("random.txt", "a") as outfile:
        outfile.write(str(random.randint(0, 100)) + "\n")
        