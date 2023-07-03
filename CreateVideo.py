import os
import cv2

path="Images/"
images=[]
for i in os.listdir(path):
    os.splittext(file)

if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name=path+"/"+file

print(file_name)

images.append(file_name)
count=len(images)
frame=cv2.imread(images[0])

frame.shape(images)
size=(width,height)

print(size)

out=cv2, VideoWriter()

videoname=Project.avi
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
fps=0.8
Size=size

out=cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVC'), 0.8,size)
for i in range(0,count-1):
    cv2.imread(images)
    out.write()
print('Done')