import cv2
import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

good_image = 1


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=10, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        if ((x2 - x1) > 120):
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    return


def filtering(image):
    import imutils

    global good_image

    resized = imutils.resize(image, 200)
    (h, w) = resized.shape[:2]
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 5, 50, 50)
    ruta = gray[0:h / 2 - 30, (w / 2):w]

    #ruta2 = cv2.adaptiveThreshold(ruta, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, -10)
    _, ruta2 = cv2.threshold(ruta, 150, 255, cv2.THRESH_BINARY)
    # ruta2=cv2.adaptiveThreshold(ruta, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 19)

    rutaq = imutils.resize(ruta2, 200)
    rutar = cv2.equalizeHist(rutaq)
    rutarx = imutils.resize(ruta2, 200)

    contours, _ = cv2.findContours(rutarx, 1, 2)[-2:]
    i = 1000
    j = 0
    k = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (h > 60 or h < 20) and (w > 120 or w < 60):
            continue

        if x < i:
            i = x
            j = y
            if h > 40:
                k = h
            else:
                k = 50
    final = rutar[j - 15:j + k, i:i + 180]

    try:
        finalr = imutils.resize(final, 250)
        return finalr

    except ZeroDivisionError as error:
        good_image = 0
        print "Divided by Zero"

    except cv2.error:
        good_image = 0
        print "Error de OpenCV"

    return final


def nothing(*arg):
    pass


if __name__ == '__main__':

    import os.path
    import time

    if os.path.isfile("camion.jpg"):
        os.remove("camion.jpg")

    cv2.namedWindow('Camara')
    cv2.createTrackbar('Brightness', 'Camara', 1, 255, nothing)
    cv2.createTrackbar('Contrast', 'Camara', 1, 255, nothing)

    cascade = cv2.CascadeClassifier("cascade.xml")
    nested = cv2.CascadeClassifier("cascade3.xml")

    cam = cv2.VideoCapture(0)
    image_saved = 0

    while True:
        _, img = cam.read()

        Brillo = cv2.getTrackbarPos('Brightness', 'Camara')
        Contsraste = cv2.getTrackbarPos('Contrast', 'Camara')

        img = cv2.addWeighted(img, 1. + Contsraste / 127., img, 0, Brillo - Contsraste)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            if (x2 - x1) > 200:
                crop_img = img[y1:y2, x1:x2]
                cv2.imshow("cropped", crop_img)

                if image_saved == 0:
                    image_saved = 1
                    cv2.imwrite("camion.jpg", crop_img)
        time.sleep(0.05)
        if os.path.isfile("camion.jpg") and good_image:
            numbers = filtering(cv2.imread("camion.jpg"))

            # kernel = np.ones((3, 3), np.uint8)
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

            # img_morf = cv2.morphologyEx(numbers, cv2.MORPH_OPEN, kernel, iterations=1)
            img_morf = cv2.morphologyEx(numbers, cv2.MORPH_CLOSE, kernel, iterations=2)


            # cv2.imshow("ruta", numbers)
            #cv2.imshow("ruta", img_morf)
            cv2.imwrite("ruta.jpg", img_morf)
            time.sleep(0.2)
            tess_temp = pytesseract.image_to_string(Image.open('ruta.jpg'))
            tess = ""
            for element in tess_temp:

                if element.isdigit():
                    tess = tess + element
            print tess
            #comando = "echo " + '"' + tess + '"' + " | festival --tts"
            #os.system(comando)
            break

        cv2.imshow('Camara', vis)
        if 0xFF & cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
