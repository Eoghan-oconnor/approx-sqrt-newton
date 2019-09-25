# Adapted from https://tour.golang.org/flowcontrol/8

def sprt(x):
    # Inital guess
    z = 1.0
    # Keep getting better est. for the square root of x, until you are within 2 decimal places 
    while abs(z*z - x) >= 0.01:
        # Get a better approximation for the square root 
    z -= (z*z - x) / (2*z)


    return z

    sqrt(8.0)