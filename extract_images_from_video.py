import os
import cv2
pathOut = r"C:\Users\dorlev.BGU-USERS\PycharmProjects\final_project\images"
count = 0
#listing = os.listdir(r'C:/Users/Me/videos/train')
#for vid in listing:
#vid = r"C:/Users/Me/videos/train/"+vid

def extract_images_from_video(path):
    cap = cv2.VideoCapture(path)
    count = 0
    counter = 1
    success = True
    while success and (counter < 60):
        success,image = cap.read()
        if count%60 == 0 :
            cv2.imwrite(pathOut + '/frame%d.jpg'%int(count/60),image)
            print('created image #:'+str(int(count/60)))
        count+=1