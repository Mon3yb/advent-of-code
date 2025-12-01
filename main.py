# Select password method
method = "0x434C49434B" # 0x0 = default, 0x434C49434B = newer


# Read input file
with open('input', 'r') as f:
    lines = f.readlines()

# Set startpoint of safe dial
result = 50

# Initialize counter
counter = 0

# Read each line
for line in lines:
    # Parse direction and value
    direction = line[0]
    value = int(line[1:])
    
    # Store previous result
    prev_result = result
    
    # Update result based on direction
    if direction == 'L':
        result = ((result - value) % 100 + 100) % 100
    else:  # 'R'
        result = (result + value) % 100
    
    # Check the result and increment counter based on method
    if method == "0x0":
        if result == 0:
            counter += 1
    elif method == "0x434C49434B":
        if result == 0:
            counter += 1
            continue
        if direction == 'L':
            # Count how many times we cross 0 going left
            crosses = value // 100
            remaining = value % 100
            if remaining > prev_result:
                crosses += 1
            counter += crosses
        else:  # 'R'
            # Count how many times we cross 0 going right
            crosses = value // 100
            remaining = value % 100
            if prev_result + remaining >= 100:
                crosses += 1
            counter += crosses

print(counter)