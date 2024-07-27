# import re

# # Read the grid from the input file
# grid = open('advent2.txt').read().splitlines()

# # Read the engine schematic grid from the input file
# # Define a function to get valid neighbors for a given cell in the grid
# # Initialize variables to track the sum of part numbers and gears with associated numbers
# # Iterate through each line of the grid
#     # Find matches of numbers in the line
#     # For each match, extract the number and initialize flags
#     # Iterate through characters in the match range
#         # Check valid neighbors of the current cell
        
#         # If the character is not a digit or period, set flags accordingly
#         # If the character is a gear symbol and not already a gear, update gears dictionary
#     # If the match represents a part number, add it to the sum
# # Calculate the product of part numbers for gears with exactly two numbers


# def get_valid_neighbors(x, y):
#     valid_neighbors = []
#     # defining the relative coordinates of neighboring cells
#     relative_neighbor_coordinates = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
#     for relative_x, relative_y in relative_neighbor_coordinates:
#         neighbor_x, neighbor_y = x + relative_x, y + relative_y
#         # Check if the neighbor is within the grid boundaries
#         if (0 <= neighbor_x < len(grid[0])) and (0 <= neighbor_y < len(grid)):
#             valid_neighbors.append((neighbor_x, neighbor_y))
#     return valid_neighbors

# # Initialize variables
# sum_of_part_numbers, gears_dict = 0, {}

# # Iterate through each line of the grid
# for current_y, line_content in enumerate(grid):
#     for match_obj in re.finditer(r'(\d+)', line_content):
#         # Extract the number from the match
#         current_number, is_part_number, is_gear = int(match_obj.group()), False, False
#         # Iterate through the characters in the match range
#         for current_x in range(match_obj.start(), match_obj.end()):
#             # Check neighbors of the current cell
#             for neighbor_x, neighbor_y in get_valid_neighbors(current_x, current_y):
#                 current_char = grid[neighbor_y][neighbor_x]
#                 # Skip digits and periods
#                 if current_char.isdigit() or current_char == '.':
#                     continue
#                 is_part_number = True
#                 # Check if the character is a gear symbol
#                 if current_char == '*' and not is_gear:
#                     # Update gears dictionary
#                     if (neighbor_x, neighbor_y) not in gears_dict:
#                         gears_dict[neighbor_x, neighbor_y] = [current_number]
#                     else:
#                         gears_dict[neighbor_x, neighbor_y].append(current_number)
#                     is_gear = True
#         # If the current match represents a part number, add it to the sum
#         if is_part_number:
#             sum_of_part_numbers += current_number

# # Calculate the product of part numbers for gears with exactly two numbers
# product_of_part_numbers = 0
# for gear_numbers in gears_dict.values():
#     if len(gear_numbers) == 2:
#         product_of_part_numbers += gear_numbers[0] * gear_numbers[1]


# print(sum_of_part_numbers)  
# print(product_of_part_numbers)  

import sys
import re
from collections import defaultdict
D = open("advent2.txt").read().strip()
lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)
p2 = 0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)