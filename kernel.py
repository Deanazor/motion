import numpy as np

def cross(size):
    """
    Create cross-shaped kernel/filter
    """
    kernel = np.zeros((size, size))
    mid = int(size / 2.0)

    kernel[mid] = np.ones(size)
    kernel[:, mid] = 1

    return kernel

  
def generate_kernel(size, kind=None):
    """
    To generate kernel
    """
    if size%2 == 0:
        raise ValueError("Well, it's not like the size can't be even, but just try something odd, baka")

    kinds = ['square', 'cross']
    if kind not in kinds:
        raise ValueError("Unrecognized kind {}, try something between {}".format(kind, kinds))

    this_kernel = np.ones((size,size), dtype=np.int) if kind == kinds[0] else cross(size)
    return this_kernel