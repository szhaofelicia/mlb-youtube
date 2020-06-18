import os
import json
import string
import random
import subprocess


save_dir = '/media/felicia/Data/mlb-youtube/full_videos/'
with open('data/mlb-youtube-segmented.json', 'r') as f:
    data = json.load(f)
    for entry in data:
        yturl = data[entry]['url']
        ytid = yturl.split('=')[-1]

        if os.path.exists(os.path.join(save_dir, ytid+'.mp4')):
            continue

        # cmd = 'youtube-dl -f mkv '+yturl+' -o '+os.path.join(ytid+'.mkv')
        cmd = 'youtube-dl -f mp4 '+yturl+' -o '+os.path.join(save_dir,ytid+'.mp4')
        os.system(cmd)

        # print(ytid)
        # print(yturl)
        # break
    
    # for key,entry in data.items():
    #     # print(key,value)
    #     # break
    #     yturl = entry['url']
    #     ytid = yturl.split('=')[-1]

    #     if os.path.exists(os.path.join(save_dir, ytid+'.mkv')):
    #         continue

    #     cmd = 'youtube-dl -f mkv '+yturl+' -o '+os.path.join(ytid+'.mkv')
    #     os.system(cmd)


    """
    youtube-dl --list-formats https://www.youtube.com/watch?v=RHlEdXq2DuI

    """