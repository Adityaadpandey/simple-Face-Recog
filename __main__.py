import face_recognition
import cv2
import os
import run
# import numpy as np

cap = cv2.VideoCapture(-1)

l1 = []
di1= r'Image/'


count1 = 0
dir_path = di1
for path in os.scandir(dir_path):
    if path.is_file():
        count1 += 1
# print('file count:', count)
for i in range(0,count1):
    a = str(i)+'.jpg'
    img = face_recognition.load_image_file(di1+a)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodingElon = face_recognition.face_encodings(img)[0]
    l1.append(encodingElon)



# if 'name' is 
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    try:
        rfaceLoc = face_recognition.face_locations(img)[0]
        cv2.rectangle(img, (rfaceLoc[3], rfaceLoc[0]),
              (rfaceLoc[1], rfaceLoc[2]), (255, 0, 0), 2)
        encodingElon = face_recognition.face_encodings(img)[0]
        results = face_recognition.compare_faces(l1, encodingElon)
        # print(results)
        l = len(results)
        # results = str(results)
        # rs1 = results.replace('True', 1)
        # rs2 = rs1.replace('False', 0)
        # rs3 = rs2.replace('[', '')
        # rs4 = rs3.replace(']', '')
        # rs5 = rs4.replace(' ', '')
        sum = 0
        for i in range(0,l):
            if results[i] == True:
                sum = sum + 1
        total = sum/l
        print(total)
        if total > 0.9:
            cv2.putText(img, 'Mr. Aditya', (rfaceLoc[3], rfaceLoc[0]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            run.run()
            break
    except:
        pass
    cv2.imshow("Face", img)
    cv2.waitKey(1)
