import time
from cv2 import resize, INTER_CUBIC
from functions import bgr2gray, m_frame_difference, s_frame_difference
from test_conv import f_convolution, f_opening
from kernel import generate_kernel
from morphology import opening, convolution

def m_detect(bgs, fg):
    """
    Function for multiple background difference

    quoted from a certain explosion girl:
    Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson.
    The time of awakening cometh.
    Justice, fallen upon the infallible boundary, appear now as an intangible distortions!
    Dance, dance, dance!
    I desire for my torrent of power a destructive force: a destructive force without equal!
    Return all creation to cinders, and come from the abyss!
    This is the mightiest means of attack known to man, the ultimate attack magic!
    """
    start = time.time()

    # resize
    dim = (256,144)
    bgs = [resize(bg, dim, interpolation=INTER_CUBIC) for bg in bgs]
    fg = resize(fg, dim, interpolation=INTER_CUBIC)

    # grayscale
    gray_bgs = [bgr2gray(bg) for bg in bgs]
    gray_fg = bgr2gray(fg)

    # frame difference & Thresholding
    img_diff = m_frame_difference(gray_bgs, gray_fg)

    # find the line
    open_k = generate_kernel(5, 'cross')
    open_img = f_opening(img_diff, open_k)
    dilate_k = generate_kernel(5, 'square')
    dilate_img = f_convolution(open_img, dilate_k, dilate=True)
    
    # draw the line
    mask = (dilate_img - open_img).astype(bool)
    line_color = [150,0,0]
    fg[mask] = line_color

    end = time.time()

    print("Detection process takes {}s to run".format(end-start))
    return fg

def detect(bg, fg):
    """
    Function for single background difference

    quoted from a certain explosion girl:
    Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson.
    The time of awakening cometh.
    Justice, fallen upon the infallible boundary, appear now as an intangible distortions!
    Dance, dance, dance!
    I desire for my torrent of power a destructive force: a destructive force without equal!
    Return all creation to cinders, and come from the abyss!
    This is the mightiest means of attack known to man, the ultimate attack magic!
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
    img_diff = s_frame_difference(gray_bg, gray_fg)

    # find the line
    open_k = generate_kernel(5, 'cross')
    open_img = opening(img_diff, open_k)
    dilate_k = generate_kernel(5, 'square')
    dilate_img = convolution(open_img, dilate_k, dilate=True)
    
    # draw the line
    mask = (dilate_img - open_img).astype(bool)
    line_color = [150,0,0]
    fg[mask] = line_color

    end = time.time()

    print("Detection process takes {}s to run".format(end-start))
    return fg