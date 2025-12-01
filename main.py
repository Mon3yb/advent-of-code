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
        result = (result - value) % 100
    else:  # 'R'
        result = (result + value) % 100
    
    # Check if result is 0 and increment counter based on method
    if method == "0x0":
        if result == 0:
            counter += 1
    elif method == "0x434C49434B":
        # Count if we land on 0
        if result == 0:
            counter += 1
        # Count if we pass through 0
        if direction == 'L':
            if prev_result < value % 100:
                counter += 1
        else:  # 'R'
            if prev_result + value >= 100:
                counter += 1

print(counter)