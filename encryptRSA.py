# Define the constants
modulus = 1964556481
exponent = 456899
bases = [7332, 6577, 3267, 7986, 7368, 4957, 3283, 8089]

# Calculate each base^exponent % modulus
results = [pow(base, exponent, modulus) for base in bases]

# Display the results
for i, result in enumerate(results, start=1):
    print(f"C{i} = {result}")
