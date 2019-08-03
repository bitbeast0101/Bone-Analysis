import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import io
from skimage import measure 
from skimage.measure import label, regionprops
from skimage.color import label2rgb
import math
import cv2

def execute(file1):
    #Pink
    img=np.asarray(io.imread(file1))
    image= cv2.cv2.cvtColor(img, cv2.cv2.COLOR_BGR2GRAY)
    lower = (65,39,85)
    upper =(221,102,255)
    mask = cv2.cv2.inRange(img, lower, upper)
    result = cv2.cv2.bitwise_and(image, image, mask=mask)
    n_white_pix = np.sum(result != 0)
    width,height=image.shape
    totalpixels=width*height
    percentwhite=(float(n_white_pix)/totalpixels)*100
    head="Mature Bone, Immature bone, Void spaces"
    data=np.zeros((3,3))
    data[0,0]=percentwhite 
    ofp = 'output.png'
    ofc= 'Results.csv'
    io.imsave(ofp,result)
    print("done")
    post=n_white_pix
    
    #Blue
    lower = (0,0,10)
    upper =(105,30,121)
    mask = cv2.cv2.inRange(img, lower, upper)
    result = cv2.cv2.bitwise_and(image, image, mask=mask)
    n_white_pix = np.sum(result != 0)
    percentwhite=(float(n_white_pix)/totalpixels)*100
    data[0,1]=percentwhite 
    ofp1 = 'output1.png'
    io.imsave(ofp1,result)
    print("done")
    post=post+n_whit_pix;
    
    #White
    n_white_pix = totalpixels-post
    percentwhite=(float(n_white_pix)/totalpixels)*100
    data[0,2]=percentwhite 
    ofp2 = 'output2.png'
    np.savetxt(ofc, data, delimiter=',', header=head, comments="")
    io.imsave(ofp2,result)
    print("done")
    
    
    return {'image1': ofp,'image2': ofp1, 'image3': ofp2, 'CSV' : ofc}

# Test code locally
if __name__ == "__main__":
    execute("input/x.jpg")

    
    