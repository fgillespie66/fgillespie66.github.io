import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


fnames = ["C:/Users/Fiona Gillespie/Documents/Calligraphy_Code/IMG_20230502_100633833.jpg"]
save_to = "C:/Users/Fiona Gillespie/Documents/Calligraphy_Code/"
visuals = False
background_color_rgb = np.array([13., 24., 150.]) #(0, 0, 0) #
char_color_tuple = (255, 255, 255)
character_color_rgb = np.array(char_color_tuple) #(255,215,0)#(255,140,0)#

for fname in fnames:
    im = cv2.imread(fname)

    # calibrate "white"
    top_corner = im[0:10, 0:10, :]

    paper_color = np.mean(top_corner, axis=(0, 1))
   
    recolored = np.maximum(np.zeros(im.shape), (1.0 - im/paper_color))*(character_color_rgb-background_color_rgb) + background_color_rgb
    
    # cast to int (very important!)
    recolored = recolored.astype(int)

    # add border
    top = int(0.05 * im.shape[0])  # shape[0] = rows
    bottom = top
    left = int(0.05 * im.shape[1])  # shape[1] = cols
    right = left
    bordered = cv2.copyMakeBorder(recolored, top, bottom, left, right, cv2.BORDER_CONSTANT, None, char_color_tuple)


    
    # save image
    imname = os.path.basename(fname)
    save_name = save_to + "recolored_clean_" + imname
    print(save_name)
    print(type(bordered))
    recolored_bgr = cv2.cvtColor(np.float32(bordered), cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_name, recolored_bgr)


    continue 


    # old version--------------------------------

    # hsv = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    # plt.imshow(hsv)
    # plt.show()

    mask = cv2.inRange(im, (0, 0, 0), (100, 100, 100))
    if visuals:
        plt.imshow(mask)
        plt.show()

    d = 5
    e = 3
    kerneld = np.ones((d, d), np.uint8)
    kernele = np.ones((e, e), np.uint8)


    for i in range(1):
        # mask = cv2.erode(mask, kernele)
        mask = cv2.dilate(mask, kerneld)

    # mask = cv2.erode(mask, kernele)
    # for i in range(2):
    #     mask = cv2.dilate(mask, kerneld)
    if visuals:
        plt.imshow(mask)
        plt.show()


    mask_indices = np.nonzero(mask)

    recolored = np.zeros((im.shape), np.uint8)
    recolored[:, :] = background_color_rgb
    recolored[mask_indices] = character_color_rgb
    if visuals:
        plt.imshow(recolored)
        plt.show()

    # add border
    top = int(0.05 * im.shape[0])  # shape[0] = rows
    bottom = top
    left = int(0.05 * im.shape[1])  # shape[1] = cols
    right = left
    bordered = cv2.copyMakeBorder(recolored, top, bottom, left, right, cv2.BORDER_CONSTANT, None, character_color_rgb)
    if True:
        plt.imshow(bordered)
        plt.show()
    
    # # save image
    # imname = os.path.basename(fname)
    # save_name = save_to + "/recolored_golden_gold_" + fname
    # # print(save_name)
    # recolored_bgr = cv2.cvtColor(bordered, cv2.COLOR_RGB2BGR)
    # cv2.imwrite(save_name, recolored_bgr)




