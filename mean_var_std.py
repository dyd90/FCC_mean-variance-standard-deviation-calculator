import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr = np.array(list)
    matrix = np.array(list).reshape(3,3)
    #print(matrix)
    #print(matrix.max(0))
    #print(matrix.max(1).reshape(1,3))

    calculations = {}
    calculations['mean'] = [matrix.mean(0).tolist(), matrix.mean(1).reshape(1,3).tolist()[0], arr.mean()]    
    calculations['variance'] = [matrix.var(0).tolist(), matrix.var(1).reshape(1,3).tolist()[0], arr.var()]
    calculations['standard deviation'] = [matrix.std(0).tolist(), matrix.std(1).reshape(1,3).tolist()[0], arr.std()]
    calculations['max'] = [matrix.max(0).tolist(), matrix.max(1).reshape(1,3).tolist()[0], max(arr)]
    calculations['min'] = [matrix.min(0).tolist(), matrix.min(1).reshape(1,3).tolist()[0], min(arr)]
    calculations['sum'] = [matrix.sum(0).tolist(), matrix.sum(1).reshape(1,3).tolist()[0], sum(arr)]
    #print(calculations)
    return calculations


#print(calculate([2,6,2,8,4,0,1,5,7]))
