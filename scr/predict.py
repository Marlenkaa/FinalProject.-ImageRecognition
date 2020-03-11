import json
from keras.models import load_model
from keras.models import model_from_json
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import operator

def objectDetection(image_path):
    ''' Recognice object in a given image ''' 

    # load model 
    
    model = load_model('./models/seventh_model_better.h5')

    # image preprocessing 

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(64,64))
    image = image.astype('float32') / 255
    
    # predict

    pred = model.predict(np.expand_dims(image,axis=0))[0]
    class_names = ['cuchara','cuchillo','cuenco','hervidor','pelador','ruido','sarten','taza','tenedor','tostadora']

    predictions = {}
    for obj in class_names:
        predictions[obj] = pred[class_names.index(obj)]
    print(f'{max(predictions.items(), key=operator.itemgetter(1))[0]}: {max(predictions.items(), key=operator.itemgetter(1))[1]}')
    plt.imshow(image);
  
  
  
  