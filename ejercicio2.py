import  random as a
from random import randint

vector_1 = []
vector_2 = []
vector_3 = []

for i in range(15):
    vector_1.append(a.randint(0,100))
    vector_2.append(a.randint(0,100))
    vector_3.append(vector_1[i] + vector_2[i])

print(f"El vector 1 {vector_1} + El vector 2 {vector_2}")
print(f"La suma de los elementos es: {vector_3}  ")

