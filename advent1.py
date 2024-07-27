def run_part1():
    with open("advent1.txt", "r") as file:
        lines = file.readlines()
        total_sum = 0
        for line in lines:
            digits = [int(char) for char in line if char.isdigit()]
            number = int(f"{digits[0]}{digits[-1]}")
            total_sum += number
    return total_sum

print(run_part1())

# import re

# def extract_digits(line):
#     digit_mapping = {
#         'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
#         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
#     }

#     for word, digit in digit_mapping.items():
#         line = line.replace(word, digit)

#     numerical_digits = [int(digit) for digit in re.findall(r'\d', line)]

#     return numerical_digits

# def calculate_calibration_value(line):
#     digits = extract_digits(line)
#     return int(''.join(map(str, digits)))

# def main():
#     file_path = "advent1.txt"  # Replace with the path to your text file
#     with open(file_path, 'r') as file:
#         input_data = file.readlines()

#     total_calibration_value = sum(calculate_calibration_value(line) for line in input_data)

#     print("Sum of calibration values:", total_calibration_value)

# if __name__ == "__main__":
#     main()
