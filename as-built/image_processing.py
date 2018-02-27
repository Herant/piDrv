import numpy as np
import cv2
from filters import canny, gaussian_blur, hough_lines, region_of_interest, grayscale, weighted_img

def process_image(image):

    grayscaleImage = grayscale(image)

    blurredImage = gaussian_blur(image, 11)

    edgesImage = canny(blurredImage, 40, 50)

    height = image.shape[0]
    width = image.shape[1]
    vertices = np.array( [[
                [3*width/4, 3*height/5],
                [width/4, 3*height/5],
                [40, height],
                [width - 40, height]
            ]], dtype=np.int32 )
    regionInterestImage = region_of_interest(edgesImage, vertices)

    #test_roi = region_of_interest(edgesImage, vertices)
    #cv2.imshow('Region Of Interest', test_roi)

    lineMarkedImage = hough_lines(regionInterestImage, 1, np.pi/180, 40, 30, 200)

    return weighted_img(lineMarkedImage, image)
