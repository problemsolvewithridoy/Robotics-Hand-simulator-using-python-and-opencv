
# Robotics Hand Simulator using Python and openCV

This project is a hand simulator for robotics applications, built with Python and a number of computer vision libraries. Using the CVZone and Mediapipe modules, the simulator tracks the movement of the user's hand and fingers in real-time, then maps these movements onto a 3D hand model. The OpenCV library is used for image processing and computer vision tasks.

The simulator is designed to be easy to use and customizable. It includes a number of built-in hand poses and gestures, such as a closed fist, open palm, and pointing finger, which can be modified or expanded as needed. The simulator also allows the user to adjust the lighting and color of the 3D model, as well as the camera angle and perspective.

This project is ideal for robotics students, researchers, or enthusiasts who want to experiment with hand tracking and motion control in a virtual environment. With its intuitive interface and powerful tracking capabilities, the simulator is a valuable tool for exploring the possibilities of robotics and human-machine interaction.

let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
pip install cvzone==1.4.1
pip install mediapipe==0.8.3.1
```
    
## Deployment

To deploy this project run

```bash
# Please Subscribe my youtube channel "@problemsolvewithridoy"
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
```
## Note:You need to store these images in your project folder

![sfs](https://user-images.githubusercontent.com/123636419/232227755-5b919f9b-f34b-414b-8b9b-e086ac0f83a8.PNG)
## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

