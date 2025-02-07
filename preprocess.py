'''This python file preprocesses the scripts saved in generate.py, then saves the preprocessed images in the same image folder'''

import cv2
import matplotlib.pyplot as plt

def pre(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0  # Normalize to [0, 1]
    return img

    # Process and display images
def write_prep():
    for i in range(3):
        path = fr'images\original\image{i+1}.png'
        preprocessed_img = pre(path)
        
        # Save the preprocessed image
        cv2.imwrite(fr'images\preprocessed\preprocessed_{i+1}.png', (preprocessed_img * 255).astype('uint8'))  # Convert back to uint8 for saving
        
        # Display the image using matplotlib
        plt.imshow(preprocessed_img, cmap='gray')
        plt.title(f'Preprocessed Image {i+1}')
        plt.show()