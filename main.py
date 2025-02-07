import  preprocess,generate
import os
import matplotlib.pyplot as plt
import cv2
# generate images
generate.gen()

for i in os.listdir('images/original'):
    img_path = os.path.join('images/original', i)
    img = cv2.imread(img_path)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(f'original image')
    plt.show()
#preprocess and save images
preprocess.write_prep()