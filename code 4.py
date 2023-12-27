import math

def quadratic_solution(a, b, c):
    delta = b**2 - 4*a*c  # Use '*' for multiplication, not '%'
    if delta >= 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    else:
        return "Complex roots - No real solution"

coefficient_sets = [(2, -6, 1), (1, 4, -6), (-1, 6, -4)]

for coefficients in coefficient_sets:
    a_set, b_set, c_set = coefficients
    roots_set = quadratic_solution(a_set, b_set, c_set)
    print(f"Set input roots: {roots_set}")

