import Augmentor
import cv2
import matplotlib.pyplot as plt
from data_process import load_data
from tensorflow.keras.utils import to_categorical

#Was used for testing data augmentation...

def getAugmentorPipeline():
        p = Augmentor.Pipeline()
        #stack operations...
        p.zoom(probability=0.25,min_factor=0.75,max_factor=1.25)
        p.random_brightness(probability=0.25,min_factor=0.75,max_factor=1.25)
        p.flip_left_right(probability=0.25)
        p.rotate(probability=0.25,max_left_rotation=10,max_right_rotation=10)
        p.shear(probability=0.25, max_shear_left=10, max_shear_right=10)
        p.random_erasing(probability=0.25,rectangle_area=0.25)
        return p

def draw_img_from_array(img_array):
    rgb_img = cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_img,interpolation='nearest')
    plt.show()

p = getAugmentorPipeline()
#stack operations...
p.random_brightness(probability=0.5,min_factor=0.75,max_factor=1.25)
p.flip_left_right(probability=0.5)
p.rotate(probability=0.5,max_left_rotation=10,max_right_rotation=10)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
#p.zoom(probability=0.25, min_factor=1.1, max_factor=1.5)
p.random_erasing(probability=0.5,rectangle_area=0.25)

(X_train,Y_train),(_ , _) = load_data()
Y_train = to_categorical(Y_train,3)
g = p.keras_generator_from_array(X_train,Y_train,batch_size=10,scaled=False)
X,y = next(g) #returns 10 outputs, because batchsize = 10
