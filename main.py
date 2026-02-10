import cv2
import os

# Getting a list of all video files in the inputs folder
files = [f for f in os.listdir("inputs/") if os.path.isfile("inputs"+'/'+f)]
print(files)

for file in files:
    video = cv2.VideoCapture("inputs/" + file)

    print(file)
    
    if video.isOpened():

        frame_number = 0
        
        while True:

            print(frame_number)

            ret, frame = video.read()

            if not ret:
                break

            frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imwrite("outputs/" + file + "_frame_" + str(frame_number) + ".jpg", frame_grayscale)

            frame_number += 1