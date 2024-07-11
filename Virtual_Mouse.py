import cv2
import time
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
index_y = 0
pTime = 0
middle_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    #convert the frame into rgb color
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand,mphands.HAND_CONNECTIONS)

            landmarks = hand.landmark
            
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                #for index finger
                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(255,255,0),thickness=cv2.FILLED)
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                 #for middle finger
                if id == 12:
                     cv2.circle(img=frame,center=(x,y),radius=10,color=(0,0,255),thickness=cv2.FILLED)
                     middle_x = screen_width/frame_width*x
                     middle_y = screen_height/frame_height*y

                
                #for thumb finger
                if id == 4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(255,0,0),thickness=cv2.FILLED)
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    
                    #printing the abs distances b/w index vs thumb and middle vs thumb fingers
                    print('outside', abs(index_y - thumb_y),abs(middle_y-thumb_y))

                    #checking the distance b/w thumb and index fingers
                    if abs(index_y - thumb_y) < 55:
                        pyautogui.click()
                        pyautogui.sleep(1)

                    elif abs(middle_y-thumb_y) < 45 : 
                        pyautogui.rightClick()  
                        pyautogui.sleep(1)
                        
                    elif abs(index_y - thumb_y) < 500:
                        pyautogui.moveTo(index_x, index_y)

    # frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    #display the frame
    cv2.imshow('Virtual Mouse', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
