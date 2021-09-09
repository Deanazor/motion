from cv2 import imread, cvtColor, resize, INTER_CUBIC, COLOR_BGR2RGB
import numpy as np
import time
from motion.kernel import generate_kernel
from motion.morphology import opening, convolution
from motion.functions import bgr2gray, show_img

# def main():
#     img_bg = cv2.imread("image_1.jpg")
#     img_fg = cv2.imread("image_2.jpg")
#     # img_bg = bgr2gray(img_bg)
#     # img_fg = bgr2gray(img_fg)
#     gray_img_bg = cv2.cvtColor(img_bg, cv2.COLOR_BGR2GRAY)
#     gray_img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGR2GRAY)
    
#     # img_diff = np.maximum(0, img_fg - img_bg)
#     # img_diff = np.round(img_diff/np.max(img_diff))
#     (score, diff) = compare_ssim(gray_img_bg, gray_img_fg, full=True)
#     diff = (diff * 255).astype("uint8")
#     print("SSIM: {}".format(score))

#     thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
    
#     for c in cnts:
#         # compute the bounding box of the contour and then draw the
#         # bounding box on both input images to represent where the two
#         # images differ
#         (x, y, w, h) = cv2.boundingRect(c)
#         cv2.rectangle(img_bg, (x, y), (x + w, y + h), (0, 0, 255), 2)
#         cv2.rectangle(img_fg, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     # show the output images
#     cv2.imshow("Original", img_bg)
#     cv2.imshow("Modified", img_fg)
#     cv2.imshow("Diff", diff)
#     cv2.imshow("Thresh", thresh)
#     cv2.waitKey(0)

def main():
    """
    Tolong eksperimen disini, trims
    """
    start_p = time.time()
    img_bg = imread("Pujo_diam.jpg")
    img_fg = imread("Pujo_tangan.jpg")
    # print(type(img_fg))

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