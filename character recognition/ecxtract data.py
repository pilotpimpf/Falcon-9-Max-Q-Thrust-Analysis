import cv2	
import easyocr
import csv
from datetime import datetime
from moviepy.editor import *

#trim video
vid = VideoFileClip('character recognition/videos/Starlink L25.mp4')

trimmed = vid.subclip('14:55','17:30')

trimmed.write_videofile("character recognition/videos/trim_Starlink L25.mp4",codec= 'libx264')

# extract frames
vid = cv2.VideoCapture("character recognition/videos/trim_Starlink L25.mp4")

index = 0
sec = -3
while vid.isOpened():
    ret,frame = vid.read()
    if not ret:
        break
    

    if index % 30 == 0:
        name = "character recognition/frames/starlink_l25/" + str(sec) +".png"
        print(f'Extracting frame.... {name}')
        cv2.imwrite(name, frame)
        sec += 1
    index += 1

vid.release()
cv2.destroyAllWindows()

# extract all data from frames
ts = datetime.timestamp(datetime.now())

reader = easyocr.Reader(['en'])

data = {}

for n in range(151):
    f ='character recognition/frames/starlink_l25/' + str(n) + '.png'
    result = reader.readtext(f)
    data[n] = result
    new = datetime.timestamp(datetime.now())
    interv = round(new - ts,2)
    ts = new
    print(f'{n+1} of 151 in {interv}s')


# extract speeds
t = 0

result = [[],[]]

for time in data.values():
    for n,d in enumerate(time):
        if time[n][0][3][0] < 120:
            try:
                #print(f'{int(time[n][1])}    {t}')
                result[1].append(int(time[n][1]))
                result[0].append(t)
            except: pass
    t +=1

header = ["Time", "Velocity"]
raw_data = result
data = []

for t, v in zip(raw_data[0],raw_data[1]):
    data.append([t,v])

with open('videodata.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print(result)
