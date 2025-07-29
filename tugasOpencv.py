import cv2
import numpy as np

cap = cv2.VideoCapture('shape.mp4')
segitigaMerah = segitigaHijau = segitigaBiru = segiempatMerah = segiempatHijau = segiempatBiru = lingkaranMerah = lingkaranHijau = lingkaranBiru  = 0

success, img = cap.read()

if success:
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerRed = np.array([0, 100, 100])
    upperRed = np.array([10, 255, 255])
    lowerGreen = np.array([40, 100, 100])
    upperGreen = np.array([80, 255, 255])
    lowerBlue = np.array([100, 100, 100])
    upperBlue = np.array([140, 255, 255])

    maskRed = cv2.inRange(hsv_img, lowerRed, upperRed)
    maskGreen = cv2.inRange(hsv_img, lowerGreen, upperGreen)
    maskBlue = cv2.inRange(hsv_img, lowerBlue, upperBlue)

    maskCombined = cv2.bitwise_or(maskRed, maskGreen)
    maskCombined = cv2.bitwise_or(maskCombined, maskBlue)

    contours, hierarchy = cv2.findContours(maskCombined.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len(approx) == 3:
            bentuk = 'segitiga'
        elif len(approx) == 4:
            bentuk = 'segi empat'
        else:
            bentuk = 'lingkaran'

        if cv2.contourArea(c) > 500: 
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            x1 = x - width / 2
            y1 = y - height / 2
            x2 = x + width / 2
            y2 = y + height / 2

            if np.any(maskRed[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'Merah' 
            elif np.any(maskGreen[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'Hijau' 
            elif np.any(maskBlue[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'Biru'

            if bentuk == 'segitiga' and warna == 'Merah':
                segitigaMerah += 1
            elif bentuk == 'segitiga' and warna == 'Hijau':
                segitigaHijau += 1
            elif bentuk == 'segitiga' and warna == 'Biru':
                segitigaBiru += 1               
            elif bentuk == 'segi empat' and warna == 'Merah':
                segiempatMerah += 1               
            elif bentuk == 'segi empat' and warna == 'Hijau':
                segiempatHijau += 1                
            elif bentuk == 'segi empat' and warna == 'Biru':
                segiempatBiru += 1               
            elif bentuk == 'lingkaran' and warna == 'Merah':
                lingkaranMerah += 1              
            elif bentuk == 'lingkaran' and warna == 'Hijau':
                lingkaranHijau += 1              
            elif bentuk == 'lingkaran' and warna == 'Biru':
                lingkaranBiru += 1

while True:
    success, img = cap.read()

    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue 

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerRed = np.array([0, 100, 100])
    upperRed = np.array([10, 255, 255])
    lowerGreen = np.array([40, 100, 100])
    upperGreen = np.array([80, 255, 255])
    lowerBlue = np.array([100, 100, 100])
    upperBlue = np.array([140, 255, 255])

    maskRed = cv2.inRange(hsv_img, lowerRed, upperRed)
    maskGreen = cv2.inRange(hsv_img, lowerGreen, upperGreen)
    maskBlue = cv2.inRange(hsv_img, lowerBlue, upperBlue)

    maskCombined = cv2.bitwise_or(maskRed, maskGreen)
    maskCombined = cv2.bitwise_or(maskCombined, maskBlue)

    contours, hierarchy = cv2.findContours(maskCombined.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 3:
            bentuk = 'segitiga'
        elif len(approx) == 4:
            bentuk = 'segi empat'
        else:
            bentuk = 'lingkaran'

        if cv2.contourArea(c) > 500: 
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            x1 = x - width / 2
            y1 = y - height / 2
            x2 = x + width / 2
            y2 = y + height / 2
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

            cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

            if np.any(maskRed[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'Merah' 
            elif np.any(maskGreen[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'Hijau' 
            elif np.any(maskBlue[int(y1):int(y2), int(x1):int(x2)]):
                warna = 'biru'
            cv2.putText(img, f'{bentuk} {warna}', (int(x1), int(y2+20)), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

    cv2.imshow("view", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('Segitiga Merah:', segitigaMerah)
print('Segitiga Hijau:', segitigaHijau)
print('Segitiga Biru:', segitigaBiru)
print('Segi Empat Merah:', segiempatMerah)
print('Segi Empat Hijau:', segiempatHijau)
print('Segi Empat Biru:', segiempatBiru)
print('Lingkaran Merah:', lingkaranMerah)
print('Lingkaran Hijau:', lingkaranHijau)
print('Lingkaran Biru:', lingkaranBiru)

cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
