# Adapted from https://tour.golang.org/flowcontrol/8

def sqrt(x):
    # Initial guess
    z = 1.0
    # Keep getting better est. for the square root of x, until you are within 2 decimal places 
    while abs(z*z - x) >= 0.0001:
        # Get a better approximation for the square root 
        z -= (z*z - x) / (2*z)
    return z




# Calculate the square root of 8
z = sqrt(64.0)
print(z)
# Print the square of the square of z
print(z*z) 
