with open("input.txt", "r") as input_file:
    with open("numbered.txt", "w") as output_file:
        line_number = 0
        for line in input_file:
            line_number += 1
            line = line.rstrip()
            print(f"Line {line_number}: {line}", file = output_file)