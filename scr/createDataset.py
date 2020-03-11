import cv2
import os
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import pickle

directory1 = '../dataset/videos/videos_red'

def getFrames(directory):
    '''Divide videos in frames and save them in specified directory by object'''
    # Get all videos
    for file in os.listdir(directory):
        if file.endswith('.mp4'):
            path = os.path.join(directory, file)
            object_name = os.path.basename(path)[:-4]
        # Read the video from specified path
        cam = cv2.VideoCapture(path)
        try:
            # Creating a folder named as object name
            if not os.path.exists(f'../dataset/images/{object_name}'):
                os.makedirs(f'../dataset/images/{object_name}')
            # If not created then raise error
        except OSError:
            print (f'Error while creating directory {object_name}')
        # frame count
        currentframe = 0
        while(True):
            # reading from frame
            ret,frame = cam.read()
            if ret:
                # if video is still left continue creating images
                name = f'../dataset/images/{object_name}/{object_name}' + str(currentframe) + '.jpg'
                # writing the extracted images
                cv2.imwrite(name, frame)
                # increasing counter
                currentframe += 1
            else:
                break
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()

getFrames(directory1)

directory2 = '../dataset/images'

def createDataset(directory):
    '''Create a dataset where store every image as array, it's label and path, in pickle format'''
    dataset = pd.DataFrame(columns=['label','image','path'])
    for obj in os.listdir(directory):
        for im in os.listdir(f'{directory}/{obj}/images_red'):
            print(im)
            dataset = dataset.append({'label':obj,'image':cv2.imread(f'{directory}/{obj}/images_red/{im}'),'path':f'{directory}/{obj}/images_red/{im}'},ignore_index=True)
    dataset.to_pickle('../dataset/dataset.pkl')
        
createDataset(directory2)