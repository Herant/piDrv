import cv2
from skimage import io

image = io.imread('http://192.168.1.130:8080/?action=stream')

while True:
    img = cv2.imdecode(image, -1)
    cv2.imshow('URL Image', img)
    cv2.waitKey()

'''
cap = cv2.VideoCapture("http://192.168.1.130:8080/?action=stream")
while True:
    if( cap.isOpened() ) :
        ret,img = cap.read()
        cv2.imshow("win",img)
        cv2.waitKey()

url = "http://192.168.1.130:8080/?action=stream"
img_array = io.imread(url)

#img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
while True:
    img = cv2.imdecode(img_array, -1)
    img1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('URL Image', img1)
    cv2.waitKey()
'''
