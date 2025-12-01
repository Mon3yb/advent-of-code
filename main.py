# Read input file
with open('input', 'r') as f:
    lines = f.readlines()

# Set startpoint of safe dial
result = 50

# Initialize counter
counter = 0

# Read each line
for line in lines:
    line = line.strip()
    # If the line is prefixed with L turn the dial left (subtract)
    if line.startswith('L'):
        result = (result - int(line[1:])) % 100 # rollover at -1
    elif line.startswith('R'):
    # If the line is prefixed with R turn the dial right (add)
        result = (result + int(line[1:])) % 100 # rollover at 100
    
    # Check if result is 0 and increment counter
    if result == 0:
        counter += 1

print(counter)