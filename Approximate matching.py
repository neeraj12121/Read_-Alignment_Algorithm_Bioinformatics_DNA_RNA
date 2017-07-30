import numpy as np
import data


def approximate_distance(x, y):

    D = np.zeros(shape=(len(x)+1,len(y)+1))

    for i in range(1, len(x)+1):
        D[i][0] = i


    for j in range(1,len(y)+1):
        D[0][j] = 0
        

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    return min(D[-1])  # return the min value of last low


human_genome = data.data_read('data/chr1.GRCh38.excerpt.fasta')
p ='GCTGATCGATCGTACG'
x = approximate_distance(p,human_genome)
print(x)
