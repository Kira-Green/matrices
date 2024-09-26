N = [
    [-1,1,2],
    [0,-2,-3],
    [3,2,5],
    [0,2,-2]
]

u = [2,-1,3]

uprime =[]

print("N is")
for i in range(len(N)):
    print(N[i])

print()
print("u is",u)

for i in range(len(N)): # the number of rows of N
    S = 0 # summation of pairwise multiplications
    for j in range(len(u)): # the dimension of u
        S = S + N[i][j] * u[j]
    uprime.append(S)

print()
print("u' is",uprime)  