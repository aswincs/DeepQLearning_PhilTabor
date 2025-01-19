import numpy as np

Q = {}

for i in range(4):
    for j in range(4):
        Q[(i,j)] = i + j

print(Q)
print("--------------------------------------")


A = np.array(list(Q[(1,i)] for i in range(4)))

print(A)
print('ArgMax :', np.argmax(A))
print('Max :', max(A))