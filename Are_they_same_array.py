

def comp(array1, array2):
    try:
        array1_sorted = sorted(array1)
        array2_sorted = sorted(array2)
        for i in range(len(array1_sorted)):
            if array1_sorted[i]**2 != array2_sorted[i]:
                return False
        return True
    except TypeError:
        return False
        
        
        '''
        import numpy as np
        def comp(array1, array2):
          if array1==None or array2==None:
             return False
          else:
             return False not in [i[0]**2==i[1] for i in zip(np.sort(array1), np.sort(array2))]
        '''
