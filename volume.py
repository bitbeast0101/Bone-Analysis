import os
from scipy import ndimage as ndi
from apeer_ometiff_library import io, processing
import skimage
import numpy as np

import matplotlib.pyplot as plt
import nibabel as nib 
from PIL import Image
import cv2

def execute(image_path,input_lower,input_upper):
    
    img=nib.load(image_path)
    data1=img.get_data()
    n_white_pix=0
    width,height,depth=data1.shape
    for i in range(1,depth):
        onearr=data1[:,:,i]
        img=Image.fromarray(onearr)
#        img.save('1.png')
#        img=cv2.imread('1.png',1)
        lower = (input_lower,input_lower,input_lower)
        upper =(input_upper,input_upper,input_upper)
        mask = cv2.inRange(img, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        n_white_pix = (np.sum(result != 0))+n_white_pix
    volume=width*height*depth
    percentage=n_white_pix
    percentage=(float(n_white_pix)/volume)*100
    head="Volume of Bone"
    data=np.zeros((1,1))
    ofd= 'Results.csv'
    np.savetxt(ofd, data, delimiter=',', header=head, comments="")
    
    return {'CSV' : ofd}

# Test Code locally
if __name__ == "__main__":
    execute("input/nucleiTubolin.ome.tiff",12,23)
#    execute("input/nucleiTubolin.jpg",23,23)

