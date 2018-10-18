import numpy as np
import cv2
from matplotlib import pyplot as plt


def main():

    def nothing(*arg):
        pass

    cv2.namedWindow('Feature Descriptor')
    cv2.createTrackbar('Brightness', 'Feature Descriptor', 1, 255, nothing)
    cv2.createTrackbar('Contrast', 'Feature Descriptor', 1, 255, nothing)

    fixedImage = cv2.imread('xbox Controller.jpg')

    camera = cv2.VideoCapture(0)
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(fixedImage, None)

    while True:

        brillo = cv2.getTrackbarPos('Brightness', 'Feature Descriptor')
        contsraste = cv2.getTrackbarPos('Contrast', 'Feature Descriptor')

        _, image = camera.read()
        image = cv2.addWeighted(image, 1. + contsraste / 127., image, 0, brillo - contsraste)

        kp2, des2 = orb.detectAndCompute(image, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)

        matches = sorted(matches, key=lambda x: x.distance)

        img3 = cv2.drawMatches(fixedImage, kp1, image, kp2, matches[:10], None, flags=2)
        cv2.imshow('Feature Descriptor', img3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return


if __name__ == '__main__':
    main()
