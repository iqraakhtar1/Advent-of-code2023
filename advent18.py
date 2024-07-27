import typing
import re

class P2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return P2(self.x * scalar, self.y * scalar)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    @property
    def east(self):
        return P2(1, 0)

    @property
    def south(self):
        return P2(0, -1)

    @property
    def west(self):
        return P2(-1, 0)

    @property
    def north(self):
        return P2(0, 1)

    @property
    def norm1(self):
        return abs(self.x) + abs(self.y)

directions = [P2().east, P2().south, P2().west, P2().north]

def parse(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r"([RDLU]) (\d+) \(#(.*)\)", line.strip())
            assert match, line
            direction, count, color = match.groups()
            hex_value = int(color, 16)
            yield (
                directions["RDLU".index(direction)] * int(count),
                directions[hex_value % 16] * (hex_value // 16),
            )

def part(index: typing.Literal[0, 1]):
    def solve(file_path: str):
        current = P2()
        points = [current]
        for movement in parse(file_path):
            current += movement[index]
            points.append(current)

        s = b = 0
        for i in range(len(points)):
            p, q = points[i], points[(i + 1) % len(points)]
            s += p.cross(q)
            b += (p - q).norm1
        return abs(s) // 2 + b // 2 + 1

    return solve

part1 = part(0)
part2 = part(1)

# Example usage
input_file_path = 'advent18.txt'
result_part1 = part1(input_file_path)
result_part2 = part2(input_file_path)

print("Part 1:", result_part1)
print("Part 2:", result_part2)