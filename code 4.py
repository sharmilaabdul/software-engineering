import math

def quadratic_solution(a, b, c):
    delta = b**2 - 4*a*c  # Use '*' for multiplication, not '%'
    if delta >= 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    else:
        return "Complex roots - No real solution"

a_single, b_single, c_single = 2, -6, 1
roots_single = quadratic_solution(a_single, b_single, c_single)
print(f"single set input roots: {roots_single}")