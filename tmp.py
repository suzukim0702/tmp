def transform_and_calculate(input_str):
    # Validation
    if len(input_str) != 11 or not all(c.isalnum() or c == ' ' for c in input_str):
        raise ValueError("Input must be an 11-character string with alphanumeric characters or spaces.")

    # Conversion table
    def char_to_number(c):
        if c.isdigit():
            return int(c)
        elif 'A' <= c <= 'O':
            return ord(c) - ord('A') + 1
        elif 'P' <= c <= 'Z':
            return ord(c) - ord('P')
        elif c == ' ':
            return 11
        else:
            raise ValueError("Invalid character in input.")

    # Weights
    weights = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4]

    # Transform characters to numbers and calculate weighted sum
    total = 0
    for i, char in enumerate(input_str):
        total += char_to_number(char) * weights[i]
#        print(char, char_to_number(char), weights[i], char_to_number(char) * weights[i])

    # Calculate remainder and final result
    remainder = total % 11
    result = (11 - remainder) % 10  # Ensures a single digit

    return result

# Example usage
try:
    input_string = "A1019 AAA01"  # Example input
    print(transform_and_calculate(input_string))
except ValueError as e:
    print(e)
