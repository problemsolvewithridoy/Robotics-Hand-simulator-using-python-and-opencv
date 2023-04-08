import cv2
from cvzone.HandTrackingModule import HandDetector
import os
import time

# select camera and make a fream
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# make a detector for hand
detector = HandDetector(detectionCon=0.7, maxHands= 2)

pTime = 0

# for select finger image path
img_path = "NewFingerPic"
img_list = os.listdir(img_path)

# for make a finger image list
hand_img = []
for i in img_list:
    image = cv2.imread(f"{img_path}/{i}")
    hand_img.append(image)

while True:
    success, img = cap.read()
    
    # for flip video capture
    img = cv2.flip(img, 1)

    # detect hand
    hands, img = detector.findHands(img)

    # for make FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # for print FPS in video fream 
    cv2.putText(img, f"FPS:{int(fps)}", (1100, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)

    if len(hands) == 1:
        # detect fingers
        hand_fingers = detector.fingersUp(hands[0])
        if hand_fingers == [0,0,0,0,0] :
            img[0:400, 0:400] = hand_img[0]
        elif hand_fingers == [0,1,0,0,0]:
            img[0:400, 0:400] = hand_img[1]
        elif hand_fingers == [0,1,1,0,0]:
            img[0:400, 0:400] = hand_img[2]
        elif hand_fingers == [0,1,1,1,0]:
            img[0:400, 0:400] = hand_img[3]
        elif hand_fingers == [0,1,1,1,1]:
            img[0:400, 0:400] = hand_img[4]
        elif hand_fingers == [1,1,1,1,1]:
            img[0:400, 0:400] = hand_img[5]
        else:
            img[0:400, 0:400] = hand_img[8]
        
    elif len(hands) == 2:
        img[0:400, 0:400] = hand_img[7]
    else:
        img[0:400, 0:400] = hand_img[6]

    cv2.imshow("Problem Solve With Ridoy", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break