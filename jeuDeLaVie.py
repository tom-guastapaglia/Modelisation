import numpy as np;
import time;
import os


t=np.zeros((11,11));



t[5,5]=1;
t[5,4]=1;
t[5,6]=1;
t[4,5]=1;
t[6,5]=1;
print(t);
def compteurVoisins(mat, i, j):
    compteur = 0;
    rows, cols = mat.shape;
    if i != 0 and j != 0 and mat[i-1,j-1] == 1:
            compteur = compteur + 1;
    if(i != 0 and mat[i-1,j] == 1):
            compteur = compteur + 1;
    if(i != 0 and j != cols-1 and mat[i-1, j+1] == 1):
            compteur = compteur + 1;
    if(j!= cols-1 and mat[i,j+1] == 1):
            compteur = compteur + 1;
    if(i != rows-1 and j != cols-1 and mat[i+1, j+1] == 1):
            compteur = compteur + 1;
    if(i != rows-1 and mat[i+1,j] == 1):
            compteur = compteur + 1;
    if(i != rows-1 and j != 0 and mat[i+1, j-1] == 1):
            compteur = compteur + 1;
    if(j != 0 and mat[i, j-1] == 1):
            compteur = compteur + 1;
    return compteur;

def iterations(t):
    temp=np.zeros((11,11));
    rows, cols = t.shape;
    for i in range (0,rows):
        for j in range(0, cols):
            if t[i,j] == 0 and compteurVoisins(t,i,j) == 3:
                temp[i,j] = 1;
            elif t[i,j] == 1 and compteurVoisins(t,i,j) == 2 or compteurVoisins(t,i,j) == 3:
                temp[i,j] = 1;
            else:
                temp[i,j] = 0;
    #print(temp);
    return temp;

"""
Si en vie : é ou 3 voisins reste en vie sinon meurt
Si elle est morte : Prends vie si 3 voisins
"""
a = 0;
"""
while(a < 12):

    iterations();
    print('/////////////////////////////');
    print(t);
    a = a +1;
"""
"""
for i in range(0,12):
    t = iterations(t);
    print(t);
    time.sleep(3);
"""