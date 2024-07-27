import sys
from sympy import Symbol, solve_poly_system

def main():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    dx = Symbol('dx')
    dy = Symbol('dy')
    dz = Symbol('dz')

    equations = []
    hit_times = []

    # Read input from the file
    with open('advent24.txt', 'r') as file:
        for index, line in enumerate(file, 1):
            point, velocity = line.strip().split('@')
            px, py, pz = [int(_) for _ in point.split(',')]
            vx, vy, vz = [int(_) for _ in velocity.split(',')]
            t = Symbol(f't{index}')

            equations.append(x + dx * t - px - vx * t)
            equations.append(y + dy * t - py - vy * t)
            equations.append(z + dz * t - pz - vz * t)
            hit_times.append(t)

            if index == 3:
                break

    # Solve the system of equations
    result = solve_poly_system(equations, *([x, y, z, dx, dy, dz] + hit_times))
    print(result[0][0] + result[0][1] + result[0][2])

if __name__ == '__main__':
    main() #part_2