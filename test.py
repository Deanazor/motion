def main():
    img_bg = cv2.imread("image_1.jpg")
    img_fg = cv2.imread("image_2.jpg")
    # img_bg = bgr2gray(img_bg)
    # img_fg = bgr2gray(img_fg)
    gray_img_bg = cv2.cvtColor(img_bg, cv2.COLOR_BGR2GRAY)
    gray_img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGR2GRAY)
    
    # img_diff = np.maximum(0, img_fg - img_bg)
    # img_diff = np.round(img_diff/np.max(img_diff))
    (score, diff) = compare_ssim(gray_img_bg, gray_img_fg, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img_bg, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img_fg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # show the output images
    cv2.imshow("Original", img_bg)
    cv2.imshow("Modified", img_fg)
    cv2.imshow("Diff", diff)
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)