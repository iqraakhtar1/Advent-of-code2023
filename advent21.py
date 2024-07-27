import functools
import itertools
import operator
from collections import Counter


def main():
    f = open("advent21.txt")
    lines = f.read().strip().split("\n")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


VECS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def vec_add(v1, v2):
    return tuple(map(operator.add, v1, v2))


def vec_mult(c, v):
    return tuple(map(lambda x: c * x, v))


def get_start(lines):
    start = None
    for index, i in enumerate(lines):
        for jndex, j in enumerate(i):
            if j == "S":
                start = (index, jndex)
    return start


def compute_dist(lines, start):
    dist = []
    for _, i in enumerate(lines):
        dist.append([])
        for _ in i:
            dist[-1].append(None)

    def in_map(x, y):
        return x in range(len(lines)) and y in range(len(lines[0]))

    cur_dist = 0
    frontier = {start}
    while frontier:
        new_frontier = set()
        for x, y in frontier:
            dist[x][y] = cur_dist
            for dx, dy in VECS:
                nx, ny = vec_add((x, y), (dx, dy))
                if in_map(nx, ny) and lines[nx][ny] in "S." and dist[nx][ny] is None:
                    new_frontier.add((nx, ny))
        frontier = new_frontier
        cur_dist += 1

    return dist


def part_1(lines):
    s = 0
    STEPS = 64
    start = get_start(lines)
    dist = compute_dist(lines, start)
    for i in dist:
        for j in i:
            if j is not None and j <= STEPS and j % 2 == STEPS % 2:
                s += 1
    return s


def part_2(lines):
    start = get_start(lines)

    data = len(lines)

    S = start[0]

    @functools.cache
    def _compute_dist(s):
        return compute_dist(lines, s)

    @functools.cache
    def _compute_count(start):
        dist = _compute_dist(start)
        c = Counter(itertools.chain.from_iterable(dist))
        del c[None]
        ans = []
        for i in range(max(c.keys()) + 1):
            if i < 2:
                ans.append(c[i])
            else:
                ans.append(ans[-2] + c[i])
        return ans

    def cover_square(start, steps):
        if steps < 0:
            return 0
        c = _compute_count(start)
        try:
            return c[steps]
        except IndexError:
            if (steps - len(c)) % 2 == 0:
                return c[len(c) - 2]
            else:
                return c[len(c) - 1]

    STEPS = 26501365

    n = STEPS // data + 3
    s = 0

    s += cover_square(start, STEPS)

    for i in range(n):
        steps = STEPS - (S + 1) - i * data
        s += cover_square((data - 1, S), steps)
        s += cover_square((S, data - 1), steps)
        s += cover_square((0, S), steps)
        s += cover_square((S, 0), steps)

    for i in range(n):
        m = i + 1
        steps = STEPS - (S + 1) * 2 - i * data
        s += m * cover_square((data - 1, 0), steps)
        s += m * cover_square((0, data - 1), steps)
        s += m * cover_square((0, 0), steps)
        s += m * cover_square((data - 1, data - 1), steps)
    return s


if __name__ == "__main__":
    main()