# Bitwise Operators Examples

# AND (&) Operation
a = 5    # 0101 in binary
b = 3    # 0011 in binary
result_and = a & b  # 0001 in binary, which is 1 in decimal
print(f"AND Operation: {a} & {b} = {result_and}")  # Output: 1

# OR (|) Operation  
result_or = a | b  # 0111 in binary, which is 7 in decimal
print(f"OR Operation: {a} | {b} = {result_or}")  # Output: 7

# XOR (^) Operation
result_xor = a ^ b  # 0110 in binary, which is 6 in decimal
print(f"XOR Operation: {a} ^ {b} = {result_xor}")  # Output: 6

# NOT (~) Operation
result_not = ~a  # 1010 in binary (two's complement form), which is -6 in decimal
print(f"NOT Operation: ~{a} = {result_not}")  # Output: -6

# Left Shift (<<) Operation
shift_left_1 = a << 1  # 1010 in binary, which is 10 in decimal
shift_left_2 = a << 2  # 10100 in binary, which is 20 in decimal
print(f"Left Shift Operation: {a} << 1 = {shift_left_1}")  # Output: 10
print(f"Left Shift Operation: {a} << 2 = {shift_left_2}")  # Output: 20

# Right Shift (>>) Operation
shift_right_1 = a >> 1  # 0010 in binary, which is 2 in decimal
shift_right_2 = a >> 2  # 0001 in binary, which is 1 in decimal
print(f"Right Shift Operation: {a} >> 1 = {shift_right_1}")  # Output: 2
print(f"Right Shift Operation: {a} >> 2 = {shift_right_2}")  # Output: 1

# Check if a number is odd or even
num = 5
if num & 1:
    print(f"{num} is Odd")  # Output: 5 is Odd
else:
    print(f"{num} is Even")

# Swapping two numbers without a temporary variable
a = 5
b = 3
a = a ^ b  # a becomes 6 (0101 ^ 0011 = 0110)
b = a ^ b  # b becomes 5 (0110 ^ 0011 = 0101)
a = a ^ b  # a becomes 3 (0110 ^ 0101 = 0011)
print(f"Swapped values: a = {a}, b = {b}")  # Output: a = 3, b = 5

# Setting a specific bit
num = 5  # 0101 in binary
position = 1
num_set_bit = num | (1 << position)  # Sets the bit at position 1, result is 0111 (7 in decimal)
print(f"Setting bit at position {position} in {num} = {num_set_bit}")  # Output: 7

# Clearing a specific bit
num = 5  # 0101 in binary
position = 2
num_clear_bit = num & ~(1 << position)  # Clears the bit at position 2, result is 0001 (1 in decimal)
print(f"Clearing bit at position {position} in {num} = {num_clear_bit}")  # Output: 1

# Toggling a specific bit
num = 5  # 0101 in binary
position = 1
num_toggle_bit = num ^ (1 << position)  # Toggles the bit at position 1, result is 0111 (7 in decimal)
print(f"Toggling bit at position {position} in {num} = {num_toggle_bit}")  # Output: 7
