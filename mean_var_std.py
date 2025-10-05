import numpy as np

def calculate(list):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    of a 3x3 matrix along both axes and for the flattened matrix.
    
    Args:
        list: A list containing 9 digits
        
    Returns:
        A dictionary containing the statistical calculations
        
    Raises:
        ValueError: If the list doesn't contain exactly 9 elements
    """
    # Check if list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns
            matrix.mean(axis=1).tolist(),  # mean of rows
            matrix.mean().tolist()          # mean of flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var().tolist()           # variance of flattened
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of columns
            matrix.std(axis=1).tolist(),   # std dev of rows
            matrix.std().tolist()           # std dev of flattened
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max().tolist()           # max of flattened
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min().tolist()           # min of flattened
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum().tolist()           # sum of flattened
        ]
    }
    
    return calculations
