def main():
    # Read input from console
    print("Enter tuples in format: name,age,height. Enter blank line to finish.")
    data = []
    while True:
        line = input()
        if not line:  # stop when blank line is entered
            break
        parts = line.split(",")
        if len(parts) == 3:
            name, age, height = parts[0].strip(), parts[1].strip(), parts[2].strip()
            data.append((name, int(age), int(height)))

    # Sort by name, then age, then height
    data.sort(key=lambda x: (x[0], x[1], x[2]))

    # Convert back to string format for output
    result = [(name, str(age), str(height)) for name, age, height in data]

    print(result)


if __name__ == "__main__":
    main()