import sys

n = len(sys.argv)
print("Total arguments passed:", n)


print("Name of Python script:", sys.argv[0])


sum_of_argument = 0

for i in range(1, n):
    sum_of_argument += int(sys.argv[i])

print("Result:", sum_of_argument) 
