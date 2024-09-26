from random import randrange

A = []
B = []
AB = []
BA = []
DIFF = []

# create A, B, AB, BA, DIFF together
for i in range(2):
    A.append([])
    B.append([])
    AB.append([])
    BA.append([])
    DIFF.append([])
    for j in range(2):
        A[i].append(randrange(-10,10)) # the elements of A are random
        B[i].append(randrange(-10,10)) # the elements of B are random
        AB[i].append(0) # the elements of AB are initially set to zeros
        BA[i].append(0) # the elements of BA are initially set to zeros
        DIFF[i].append(0) # the elements of DIFF are initially set to zeros

print("A =",A)
print("B =",B)
print() # print a line
print("AB, BA, and DIFF are initially zero matrices")
print("AB =",AB)
print("BA =",BA)
print("DIFF =",BA)

# let's find AB
for i in range(2):
    for j in range(2):
        # remark that AB[i][j] is already 0, and so we can directly add all pairwise multiplications
        for k in range(2):
            AB[i][j] = AB[i][j] + A[i][k] * B[k][j] # each multiplication is added

print() # print a line
print("AB =",AB)

# let's find BA
for i in range(2):
    for j in range(2):
        # remark that BA[i][j] is already 0, and so we can directly add all pairwise multiplications
        for k in range(2):
            BA[i][j] = BA[i][j] + B[i][k] * A[k][j] # each multiplication is added

print("BA =",BA)

# let's calculate DIFF = AB- BA
for i in range(2):
    for j in range(2):
        DIFF[i][j] = AB[i][j] - BA[i][j]

print() # print a line        
print("DIFF = AB - BA =",DIFF)