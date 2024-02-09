def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits

    return None

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found.")
