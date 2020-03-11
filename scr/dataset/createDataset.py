import cv2
import os
from PIL import Image
import pandas as pd
import pickle

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
            if not os.path.exists(f'../../INPUT/images/{object_name}'):
                os.makedirs(f'../../INPUT/images/{object_name}')
                print(f'{object_name} folder created')
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
                name = f'../../INPUT/images/{object_name}/{object_name}' + str(currentframe) + '.jpg'
                # writing the extracted images
                cv2.imwrite(name, frame)
                # increasing counter
                currentframe += 1
            else:
                break
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()


def getDataset(directory):
    '''Create a dataset where store every image as array, it's label and path, in pickle format'''
    dataset = pd.DataFrame(columns=['label','image','path'])
    for obj in os.listdir(directory):
        for im in os.listdir(f'{directory}/{obj}'):
            dataset = dataset.append({'label':obj,'image':cv2.imread(f'{directory}/{obj}/{im}'),'path':f'{directory}/{obj}/{im}'},ignore_index=True)
        print(f'{obj} dataset created')
    dataset.to_pickle('../../INPUT/training_dataset.pkl')