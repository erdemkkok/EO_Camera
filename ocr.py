import cv2 
import pytesseract
import numpy as np
from openpyxl import Workbook,load_workbook
sharp_kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
wb = load_workbook("Bitirme.xlsx")
ws = wb.active
def runocr(im0):
    ret,frame=im0.read()
    frame1 = cv2.resize(frame,(2880,1612),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    median=cv2.medianBlur(gray,5)
    ret, thresh2 = cv2.threshold(median, 120, 255, cv2.THRESH_TOZERO)
    sharp_img = cv2.filter2D(src=thresh2, ddepth=-1, kernel=sharp_kernel)

    #bileteral = cv2.bilateralFilter(median,9,75,75)
    edged = cv2.Canny(sharp_img, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    ret, thresh3 = cv2.threshold(edged, 200, 255, cv2.THRESH_BINARY_INV)
    data = pytesseract.image_to_data(thresh3,config='--psm 11' ,output_type='dict')#
    boxes = len(data['level'])
    for i in range(boxes):
        if(data['text'][i]=="ACFT"):
            print("Koordinat Verisi")
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            #x=x-5
            y=y
            crop_img = thresh3[y:y+h+700, x:x+w+600]
            ret, thresh4 = cv2.threshold(crop_img, 120, 255, cv2.THRESH_BINARY_INV)
            cv2.imshow("asdf",thresh4)
            data1 = pytesseract.image_to_data(crop_img, output_type='dict')
            val=data['text'][i+3]
            val1=data['text'][i+4]
            val2=data['text'][i+5]
            print(data1)
            print("deger="+val)
            print("deger1="+val1)
            print("deger2="+val2)
    print("MULTITHREAD BASARILI")
    return thresh3