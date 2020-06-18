import os

import cv2
import json
import pickle

PATH_TO_TEST_IMAGES_DIR = '/media/felicia/Data/mlb-youtube/frames_continuous/swing'
PICKLE_DIR='/media/felicia/Data/baseballplayers/pickles/'
filenames=os.listdir(PATH_TO_TEST_IMAGES_DIR)
videonames=[x[:-8] for x in filenames]
videonames=list(set(videonames))

print(len(videonames)) # 453
print(len(filenames)) # 8607

# pickle.dump(videonames,open(PICKLE_DIR+'swing_videos.pkl','wb'))
