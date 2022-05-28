import os
from torch.utils.data import Dataset
from PIL import Image
import torch
import torchvision.transforms as T

def rescale(x):
    low,high = x.min(),x.max()
    x_rescaled = (x-low)(high-low)
    return x_rescaled

def transform_back(img):
    trfb = T.Compose([
      T.Lambda(lambda x: x[0]),
      T.Normalize(mean=[0, 0, 0], std=[4.3668, 4.4643, 4.4444]),
      T.Normalize(mean=[-0.485, -0.456, -0.406], std=[1, 1, 1]),
      T.Lambda(rescale),
      #T.ToPILImage(),
  ])
    return trfb(img)




class NST_data(object):
    def __init__(self, styler_path, image_path,size=224):
        
        self.sp=styler_path
        self.ip=image_path
        self.size=size
        
    def transform(self,img1,img2,size=224):
        
        trf = T.Compose([
      T.Resize(size),
      T.ToTensor(),
      T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
      T.Lambda(lambda x: x[None]),
  ])
        return trf(img1), trf(img2)
       
    
    
    
    def build(self):
        styler=Image.open(self.sp)
        
        image=Image.open(self.ip)
        
        return self.transform(styler,image,self.size)