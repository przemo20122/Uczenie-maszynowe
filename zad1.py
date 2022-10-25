'''
import cv2
img = cv2.imread('city.jpg')
print(type(img))
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import pytesseract

# ścieżka do pytesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def image_to_string(img_path):
    img = cv2.imread(img_path)

    # Preprocessing (zmiana BGR-czarnobiały, progowanie obrazu, Rozmycie gaussowskie)
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_g = cv2.threshold(img_g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img_g = cv2.GaussianBlur(img_g, (5, 5), 0)

    ocr = pytesseract.image_to_string(img_g)
    print(ocr)


image_to_string('tekst1.png')
image_to_string('tekst2.png')
image_to_string('tekst3.png')
image_to_string('tekst4.png')
