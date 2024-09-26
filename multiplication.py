# matrix M
M = [
    [-1,0,1],
    [-2,-1,2],
    [1,2,-2]
]

# matrix N
N = [
    [0,2,1],
    [3,-1,-2],
    [-1,1,0]
]

# matrix K
K = []

for i in range(3):
    K.append([])
    for j in range(3):
        # here we calculate K[i][j]
        # inner product of i-th row of M with j-th row of N
        S = 0
        for k in range(3):
            S = S + M[i][k] * N[k][j]
        K[i].append(S)
        
print("M is")
for i in range(len(M)):
    print(M[i])
    
print()
print("N is")
for i in range(len(N)):
    print(N[i])

print()
print("K is")
for i in range(len(K)):
    print(K[i])