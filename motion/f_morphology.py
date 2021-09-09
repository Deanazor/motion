from .morphology import dilate_opt, erode_opt, opening
import numpy as np

def f_convolution(image, kernel, dilate=False, erode=False):
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

    # add padding to input
    pad_height = int(np.ceil((kernel_row - 1) / 2))
    pad_width = int(np.ceil((kernel_col - 1) / 2))
    img_pad = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
    img_pad[pad_height:img_pad.shape[0] - pad_height, pad_width:img_pad.shape[1] - pad_width] = image.copy()

    output = np.array([[dilate_opt(kernel, img_pad[row:row + kernel_row, col:col + kernel_col]) \
                        if dilate else erode_opt(kernel, img_pad[row:row + kernel_row, col:col + kernel_col]) \
                            for col in range(image_col)] for row in range(image_row)])
                
    return output

def f_opening(image, kernel):
    """
    Opening for reducing the so-called noise
    """
    eroded_img = f_convolution(image, kernel, erode=True)
    final_img = f_convolution(eroded_img, kernel, dilate=True)

    return final_img

def f_closing(image, kernel):
    """
    Closing for reduce gap between object
    """
    dilated_img = f_convolution(image, kernel, dilate=True)
    final_img = f_convolution(dilated_img, kernel, erode=True)

    return final_img