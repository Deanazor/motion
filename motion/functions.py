import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use( 'tkagg' )

def bgr2gray(img):
    """
    Transform image into grayscale
    """
    gray_w = [0.59, 0.11, 0.3]
    gray_img = img @ gray_w
    return gray_img

def show_img(img, cmap=None):
    """
    Display Image
    """
    plt.imshow(img, cmap=cmap)
    plt.show()

def log_transform(img, gamma=1):
    """
    To increase the pixel intensity
    """
    c = 255 / np.log(1 + np.max(img))
    log_img =  c * img**gamma
    # log_img = (255.0*(img/255.0))**gamma (gagal)
    return np.array(log_img, dtype=np.uint8)

def s_frame_difference(bg:np.ndarray, fg:np.ndarray):
    """
    Single Frame Difference function
    """
    # Frame Difference
    img_diff = np.maximum(0, np.abs(fg - bg))
    # Thresholding
    img_diff = (img_diff > 20).astype(int)

    return img_diff

def m_frame_difference(bgs:list, fg:np.ndarray):
    """
    Multiple Frame Difference function
    """
    # Find the cummulative difference
    img_diffs = np.sum([s_frame_difference(fg, bg) for bg in bgs], axis=0)
    # Threshold for cummulative difference
    thresh = round(len(bgs)*0.75)
    img_diffs = (img_diffs >= thresh).astype(int)

    return img_diffs