import os 
import cv2

path = "Image_Pro"

images=[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.png', '.jpg', '.gif', '.jpeg', '.jfif']:
        file_name = path + "/" + file

        print(file_name)

        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

outVid = cv2.VideoWriter("Friends.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    frame = cv2.imread(images[i])
    outVid.write(frame)
    print(i, images[i])

outVid.release()
print("DONE")