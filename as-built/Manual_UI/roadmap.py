import numpy as np
import cv2

def road_map(img, down_left_point, up_left_point, up_right_point, down_right_point):

    mask = img

    vertices = np.array([[
        [int(down_left_point[0]),int(down_left_point[1])],
        [int(up_left_point[0]),int(up_left_point[1])],
        [int(up_right_point[0]),int(up_right_point[1])],
        [int(down_right_point[0]),int(down_right_point[1])],
        [int(down_left_point[0]),int(down_left_point[1])],
        ]],dtype=np.int32)


    cv2.fillPoly(mask, vertices, 100)
    masked_image = cv2.bitwise_and(img, mask)

    return masked_image

#OPTIONAL
def grid_lines(img, down_left_point, up_left_point, up_right_point, down_right_point):

    cv2.line(img, (int(up_left_point[0]),(int(up_left_point[1]+20))),(int(up_right_point[0]),int(up_right_point[1]+20)), [0, 255, 0], 1)
    cv2.line(img, (int(up_left_point[0]-20),(int(up_left_point[1]+40))),(int(up_right_point[0]+20),int(up_right_point[1]+40)), [0, 255, 0], 1)
    cv2.line(img, (int(up_left_point[0]-40),(int(up_left_point[1]+60))),(int(up_right_point[0]+40),int(up_right_point[1]+60)), [0, 255, 0], 1)
    cv2.line(img, (int(up_left_point[0]-60),(int(up_left_point[1]+80))),(int(up_right_point[0]+60),int(up_right_point[1]+80)), [0, 255, 0], 1)
    cv2.line(img, (int(up_left_point[0]-80),(int(up_left_point[1]+100))),(int(up_right_point[0]+80),int(up_right_point[1]+100)), [0, 255, 0], 1)
