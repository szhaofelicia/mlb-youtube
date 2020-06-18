import cv2
import json


def extract_from_single_video(videoname,input_directory,output_directory):
    vidcap = cv2.VideoCapture(input_directory+videoname+'.mp4')
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite(output_directory+videoname+ "{:04d}".format(count)+".jpg", image)     # save frame as JPG file
        return hasFrames
    sec = 0
    frameRate = 0.1 # 0.5: it will capture image in each 0.5 second
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    print(videoname,sec)


# videoname='377H4PC2NSEP'
# input_directory='/media/felicia/Data/mlb-youtube/continuous_videos/'
# output_directory='/media/felicia/Data/mlb-youtube/frames/'

# extract_from_single_video(videoname,input_directory,output_directory)



input_directory='/media/felicia/Data/mlb-youtube/segmented_videos/'
output_directory='/media/felicia/Data/mlb-youtube/frames_segmented/'
# videoname='E40GRXPSLG7N'
# extract_from_single_video(videoname,input_directory,output_directory)


count=0
with open('data/mlb-youtube-segmented.json', 'r') as f:
    data = json.load(f)
    for filename in data.keys():
        if count<200 :
            print(filename)
            extract_from_single_video(filename,input_directory,output_directory)
            count+=1
        else:
            break


#############################################################


