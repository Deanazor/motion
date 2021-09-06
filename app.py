from cv2 import imread, cvtColor, resize, INTER_CUBIC, COLOR_BGR2RGB, threshold, THRESH_BINARY
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from kernel import generate_kernel
from morphology import opening, convolution

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

def detect(bg, fg):
    """
    Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson.
    The time of awakening cometh.
    Justice, fallen upon the infallible boundary, appear now as an intangible distortions!
    Dance, dance, dance!
    I desire for my torrent of power a destructive force: a destructive force without equal!
    Return all creation to cinders, and come from the abyss!
    This is the mightiest means of attack known to man, the ultimate attack magic! 
    DETECTION!!!!!! *sfx:BOOM*
    """
    start = time.time()

    # resize
    dim = (256,144)
    bg = resize(bg, dim, interpolation=INTER_CUBIC)
    fg = resize(fg, dim, interpolation=INTER_CUBIC)

    # grayscale
    gray_bg = bgr2gray(bg)
    gray_fg = bgr2gray(fg)

    # frame difference
    img_diff = np.maximum(0, np.abs(gray_fg - gray_bg))
    # thresholding
    img_diff = (img_diff > 30).astype(int) 

    # find the line
    open_k = generate_kernel(5, 'cross')
    open_img = opening(img_diff, open_k)
    dilate_k = generate_kernel(3, 'square')
    dilate_img = convolution(open_img, dilate_k, dilate=True)
    
    # draw the line
    mask = (dilate_img - open_img).astype(bool)
    line_color = [150,0,0]
    fg[mask] = line_color

    end = time.time()

    print("Detection process takes {}s to run".format(end-start))
    return fg

def main():
    """
    Tolong eksperimen disini, trims
    """
    start_p = time.time()
    img_bg = imread("Pujo_diam.jpg")
    img_fg = imread("Pujo_tangan.jpg")
    print(type(img_fg))

    dim = (256,144)
    img_bg = resize(img_bg, dim, interpolation=INTER_CUBIC)
    img_fg = resize(img_fg, dim, interpolation=INTER_CUBIC)

    gray_img_bg = bgr2gray(img_bg)
    gray_img_fg = bgr2gray(img_fg)

    # log_bg = log_transform(gray_img_bg, 0.3)
    # log_fg = log_transform(gray_img_fg, 0.3)
    # show_img(log_bg, cmap='gray')
    # show_img(log_fg, cmap='gray')
    
    
    # thresh1 = cv2.adaptiveThreshold(gray_img_bg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 101, 5)
    # thresh2 = cv2.adaptiveThreshold(gray_img_fg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 101, 5)
    # img_diff = np.abs(thresh2 - thresh1)
    img_diff = np.maximum(0, np.abs(gray_img_fg - gray_img_bg))
    # edges = cv2.Canny(img_diff,100,200)
    img_diff = (img_diff > 20).astype(int)
    # print(np.max(img_diff))

    start_m = time.time()
    open_k = generate_kernel(5, 'cross')
    open_img = opening(img_diff, open_k)
    dilate_k = generate_kernel(5, 'square')
    dilate_img = convolution(open_img, dilate_k, dilate=True)
    end_m = time.time()

    img_fg = cvtColor(img_fg, COLOR_BGR2RGB)
    # show_img(img_fg)

    mask = (dilate_img - open_img).astype(bool)
    line_color = [0,0,150]
    img_fg[mask] = line_color
    end_p = time.time()

    print("Morphological process takes {}s".format(end_m-start_m))
    print("It takes {}s for the program to run".format(end_p - start_p))
    # print("Line image content: {}".format(np.unique(mask)))
    show_img(img_diff, cmap='gray')
    # show_img(open_img, cmap='gray')
    # show_img(dilate_img, cmap='gray')
    # show_img(mask, cmap='gray')
    show_img(img_fg)
    # show_img(edges, cmap='gray')

if __name__ == "__main__":
    main()