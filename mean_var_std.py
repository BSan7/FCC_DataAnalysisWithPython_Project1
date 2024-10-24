import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    array1 = np.array(list)
    array1 = array1.reshape(3,3)   #making the 3x3 matrix
    
    calculations = {
        'mean': [array1.mean(axis = 0).tolist(), array1.mean(axis = 1).tolist(), array1.mean()],
        'variance': [array1.var(axis = 0).tolist(), array1.var(axis = 1).tolist(), array1.var()],
        'standard deviation': [array1.std(axis = 0).tolist(), array1.std(axis = 1).tolist(), array1.std()],
        'max': [array1.max(axis = 0).tolist(), array1.max(axis = 1).tolist(), array1.max()],
        'min': [array1.min(axis = 0).tolist(), array1.min(axis = 1).tolist(), array1.min()],
        'sum': [array1.sum(axis = 0).tolist(), array1.sum(axis = 1).tolist(), array1.sum()]
        }
    
    return calculations  