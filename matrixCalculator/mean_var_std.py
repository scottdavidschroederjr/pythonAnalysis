import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    calculations = {}
    npList = np.array(list)
    npList = npList.reshape(3, 3)

    mean = [0, 0, 0]
    mean[0] = npList.mean(axis = 0).tolist()
    mean[1] = npList.mean(axis = 1).tolist()
    mean[2] = npList.mean()
    
    variance = [0, 0, 0]
    variance[0] = npList.var(axis = 0).tolist()
    variance[1] = npList.var(axis = 1).tolist()
    variance[2] = npList.var()

    std = [0, 0, 0]
    std[0] = npList.std(axis = 0).tolist()
    std[1] = npList.std(axis = 1).tolist()
    std[2] = npList.std()

    max = [0, 0, 0]
    max[0] = npList.max(axis = 0).tolist()
    max[1] = npList.max(axis = 1).tolist()
    max[2] = npList.max()

    min = [0, 0, 0]
    min[0] = npList.min(axis = 0).tolist()
    min[1] = npList.min(axis = 1).tolist()
    min[2] = npList.min()

    sum = [0, 0, 0]
    sum[0] = npList.sum(axis = 0).tolist()
    sum[1] = npList.sum(axis = 1).tolist()
    sum[2] = npList.sum()

    calculations["mean"] = mean
    calculations["variance"] = variance
    calculations["standard deviation"] = std
    calculations["max"] = max
    calculations["min"] = min
    calculations["sum"] = sum


    return calculations



  
  
  