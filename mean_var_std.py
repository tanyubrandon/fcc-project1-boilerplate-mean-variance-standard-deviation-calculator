import numpy as np

def calculate(list):
    if len(list)!= 9:
      raise ValueError("List must contain nine numbers.")
    
    # list = np.array(list).reshape((3,3))

    list = np.array(list)

    list = list.reshape((3,3))
    
    
    mean_axis1 = list.mean(axis = 0).tolist()
    mean_axis2 = list.mean(axis = 1).tolist()
    mean_flattened = list.flatten().mean()
    
    var_axis1 = list.var(axis = 0).tolist()
    var_axis2 = list.var(axis = 1).tolist()
    var_flattened = list.flatten().var()
    
    
    std_axis1 = list.std(axis = 0).tolist()
    std_axis2 = list.std(axis = 1).tolist()
    std_flattened =list.flatten().std()
    
    
    max_axis1 = list.max(axis = 0).tolist()
    max_axis2 = list.max(axis = 1).tolist()
    max_flattened = list.flatten().max()
    
    min_axis1 = list.min(axis = 0).tolist()
    min_axis2 = list.min(axis = 1).tolist()
    min_flattened = list.flatten().min()
    
    min_axis1 = list.min(axis = 0).tolist()
    min_axis2 = list.min(axis = 1).tolist()
    min_flattened = list.flatten().min()
    
    
    sum_axis1 = list.sum(axis = 0).tolist()
    sum_axis2 = list.sum(axis = 1).tolist()
    sum_flattened = list.flatten().sum()
    
    
    calculations = {
        'mean':[mean_axis1,mean_axis2,mean_flattened],
        'variance':[var_axis1,var_axis2,var_flattened],
        'standard deviation':   [std_axis1,std_axis2,std_flattened],
        'max':[max_axis1,max_axis2,max_flattened],
        'min':[min_axis1,min_axis2,min_flattened],
        'sum':[sum_axis1,sum_axis2,sum_flattened]
    }
    return calculations

list = [0,1,2,3,4,5,6,7,8]


calculate(list)


  