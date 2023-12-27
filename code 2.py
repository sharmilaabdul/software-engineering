import math
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
def quadratic_solution(x):
  return a*x**2+b*x+c
print(quadratic_solution(3))