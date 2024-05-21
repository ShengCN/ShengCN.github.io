import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

parser = argparse.ArgumentParser(description='Crop for paper figure')
parser.add_argument('--file', type=str, help='input file name')
parser.add_argument('--ofile', type=str, help='output file name')
parser.add_argument('--resize', type=int, default=512, help='y center')
args = parser.parse_args()
print(args)

f = args.file
of = args.ofile
resize = args.resize
img = plt.imread(f)

# assume it is rectangle image
h,w,_ = img.shape
ratio = w/h

new_w = int(resize * ratio) 
resize_img = cv2.resize(img, (new_w, resize))
h_center = new_w // 2
resize_img = resize_img[:,h_center-resize//2:h_center+resize//2]

plt.imsave(of,resize_img)



