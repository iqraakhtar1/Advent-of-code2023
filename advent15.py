from collections import defaultdict
from typing import List, Tuple

def hash_algorithm(s: str) -> int:
    val = 0
    for ch in s:
        val += ord(ch)
        val *= 17
        val %= 256
    return val

def part1(input_string: str) -> int:
    parts = input_string.split(",")
    return sum(map(hash_algorithm, parts))

def part2(input_string: str) -> int:
    parts = input_string.split(",")
    boxes = defaultdict(list)
    
    for p in parts:
        if "=" in p:
            key, value = p.split("=")
            h = hash_algorithm(key)
            lens_list = boxes[h]
            
            found = False
            for i, (label, _) in enumerate(lens_list):
                if label == key:
                    lens_list[i] = (key, int(value))
                    found = True
                    break
            
            if not found:
                lens_list.append((key, int(value)))
        else:
            key = p[:-1]
            h = hash_algorithm(key)
            lens_list = boxes[h]
            
            for i, (label, _) in enumerate(lens_list):
                if label == key:
                    lens_list.pop(i)
                    break
    
    # compute focal power
    focal_power = 0
    for box, lens_list in boxes.items():
        for i, (_, n) in enumerate(lens_list):
            focal_power += (box + 1) * (i + 1) * n
    
    return focal_power

if __name__ == "__main__":
    with open("advent15.txt", "r") as file:
        input_data = file.read().strip()

    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))