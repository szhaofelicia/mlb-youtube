import os
import json
import string
import random
import subprocess
import multiprocessing
import cv2

def local_clip(filename, start_time, duration, output_filename, output_directory):
    end_time = start_time + duration
    command = ['ffmpeg',
               '-i', '"%s"' % filename,
               '-ss', str(start_time),
               '-t', str(end_time - start_time),
               '-c:v', 'copy', '-an',
               '-threads', '1',
               '-loglevel', 'panic',
               os.path.join(output_directory,output_filename)]
    command = ' '.join(command)

    try:
        output = subprocess.check_output(command, shell=True,
                                         stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print(err.output)
        return err.output


def wrapper(clip):
    input_directory = '/media/felicia/Data/mlb-youtube/full_videos/'
    output_directory = '/media/felicia/Data/mlb-youtube/continuous_videos/'
    duration = clip['end']-clip['start']
    filename = clip['url'].split('=')[-1]
    # print(clip.keys())
    local_clip(os.path.join(input_directory,filename+'.mp4'), clip['start'], duration, clip['clip_name']+'.mp4', output_directory)
    return 0

def wrapper_activity(clip):
    input_directory = '/media/felicia/Data/mlb-youtube/continuous_videos/'
    output_directory = '/media/felicia/Data/mlb-youtube/swing_videos/'
    video=clip['clip_name']
    duration = clip['end']-clip['start']
    cap = cv2.VideoCapture(input_directory+video+'.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    delta=duration-int(cap.get(cv2.CAP_PROP_FRAME_COUNT))/fps
    for activity in clip['annotations']:
        start, end=activity['segment']
        label=activity['label']
        if label=='swing':
            duration_ = end-start
            print(delta,start,end,duration_,os.path.join(input_directory,video+'.mp4'))
            local_clip(os.path.join(input_directory,video+'.mp4'), start-delta, duration_, video+'.mp4', output_directory)
            # break
    return 0
    

# with open('data/mlb-youtube-continuous.json', 'r') as f:
#     data = json.load(f)
#     pool = multiprocessing.Pool(processes=8)
#     # pool.map(wrapper, [data[k] for k in data.keys()])
#     for k in data.keys():
#         data[k]['clip_name']=k
#     pool.map(wrapper, [data[k] for k in data.keys()])
    

"""
O35GBDO4IA6O.mp4
"""

with open('data/mlb-youtube-continuous.json', 'r') as f:
    data = json.load(f)
    pool = multiprocessing.Pool(processes=8)
    # pool.map(wrapper, [data[k] for k in data.keys()])
    k='O35GBDO4IA6O'
    data[k]['clip_name']=k
    pool.map(wrapper_activity, [data[k]])
