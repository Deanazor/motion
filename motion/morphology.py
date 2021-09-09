import numpy as np

def dilate_opt(a,b):
    """
    Dilation operation to expand the masked image
    """
    res = np.logical_and(a,b).astype(int)
    return int(res.any())

def erode_opt(a,b):
    """
    Erotion function to do erotic....I mean to reduce the masked image
    """
    mask = a==1
    a = a[mask]
    b = b[mask]
    res = np.logical_and(a,b)
    # print(res)
    return int(res.all())

def convolution(image, kernel, dilate=False, erode=False):
    """
    Hard-coded-modified-operation convolution function
    """
    if dilate and erode:
        raise ValueError("Can't do dilation and erotion at the same time")
    if not dilate and not erode:
        raise ValueError("Dude, really? At least do dilation or erotion")
    
    # get the kernel and image shape
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    # output image/array
    output = np.zeros(image.shape)

    # add padding to input
    pad_height = int(np.ceil((kernel_row - 1) / 2))
    pad_width = int(np.ceil((kernel_col - 1) / 2))
    img_pad = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
    img_pad[pad_height:img_pad.shape[0] - pad_height, pad_width:img_pad.shape[1] - pad_width] = image.copy()
    
    # the convolution
    for row in range(image_row):
        for col in range(image_col):
            b = img_pad[row:row + kernel_row, col:col + kernel_col]
            if dilate:
                output[row, col] = dilate_opt(kernel,b)
            else :
                output[row, col] = erode_opt(kernel,b)
                
    return output

def opening(image, kernel):
    """
    Opening for reducing the so-called noise
    """
    eroded_img = convolution(image, kernel, erode=True)
    final_img = convolution(eroded_img, kernel, dilate=True)

    return final_img

def closing(image, kernel):
    """
    Closing for reduce gap between object
    """
    dilated_img = convolution(image, kernel, dilate=True)
    final_img = convolution(dilated_img, kernel, erode=True)

    return final_img