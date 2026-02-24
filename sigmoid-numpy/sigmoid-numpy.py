import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_arr = np.array(x, dtype = float)
    return 1/(1 + np.exp(-x_arr))