import numpy as np
import math
import matplotlib.pyplot as plt

def fucktorial(n:int):
    f = 1
    if n%2 == 0:
        for i in range(1,n//2+1):
            f *= 2*i
        return f
    else:
        for i in range((n-1)//2+1):
            f *= 2*i + 1
        return f

x = 100
sum = math.log(2*x)
ordered_sum = math.log(2*x)
kahan_sum = 0 
c = 0

value = math.asinh(x)
coefficients = []
nth_nom = 1

n = 0

while abs(nth_nom) >= 1e-12:
    n += 1
    nth_nom = ((-1)**n)*fucktorial(2*n-1)/(2*n*(fucktorial(2*n))*pow(x,2*n))
    coefficients.append(nth_nom)

for i in range(n):
    sum -= coefficients[i]

for i in range(n):
    y = coefficients[i]-c
    t = kahan_sum + y
    z = t - kahan_sum
    c = z - y
    kahan_sum = t
kahan_sum =  math.log(2*x) - kahan_sum


for i in range(n-1):
    for j in range(n-1-i):
        if coefficients[j] > coefficients[j+1]:
            coefficients[j],coefficients[j+1] = coefficients[j+1],coefficients[j]
for i in range(n):
    ordered_sum -= coefficients[i]


print("x:  ", x, ",    n:  ", n, ".")
print(f"f(x) = arsh(x):  {value};")
print(f"sum_1 (naive):  {sum:<15},    delta_1:  {value - sum:<15}")
print(
    f"sum_2 (ordered):  {ordered_sum:<15},    delta_2:  {value - ordered_sum:<15}")
print(
    f"sum_3 (Kahan):  {kahan_sum:<15},    delta_3:  {value - kahan_sum:<15}")