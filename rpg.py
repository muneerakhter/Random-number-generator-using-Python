# Simple Random Number Simulator (LCG)

seed = 12345  # change this for different results

def random_number(min_val, max_val):
    global seed
    a = 1103515245
    c = 12345
    m = 2**31

    seed = (a * seed + c) % m
    return min_val + (seed % (max_val - min_val + 1))


# Simulator Example
print("Random Dice Rolls:")
for i in range(5):
    print(random_number(1, 6))

print("\nRandom Coin Toss:")
for i in range(5):
    toss = random_number(0, 1)
    print("Heads" if toss == 1 else "Tails")
