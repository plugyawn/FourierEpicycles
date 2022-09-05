from rembg import remove
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

import os

from config.definitions import ROOT_DIR
INPUT_DIR = ROOT_DIR+"/data/"
OUTPUT_DIR = ROOT_DIR+"/processed_data/"

res = []

class image_process:

    def __init__(self):
        print(f"Image processing started. Reading from {INPUT_DIR}, writing to {OUTPUT_DIR}.")

    def return_img_list(self, inp_dir = "data"):
        img_list = []
        for path in os.listdir(ROOT_DIR+"/"+inp_dir):
            if os.path.isfile(os.path.join(ROOT_DIR+"/"+inp_dir, path)):
                img_list.append(path)
        return img_list

    def remove_background(self, img_list, inp_dir="data", out_dir="processed_data"):
        for img in img_list:
            input_path = f"{ROOT_DIR}/{inp_dir}/"
            output_path = f"{ROOT_DIR}/{out_dir}/"

            with open(f"{input_path}/{img}", 'rb') as i:
                with open(f"{output_path}/{img}", 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

    def edge_detect(self, img_list, inp_dir="processed_data", out_dir="final_data"):
        print(img_list)
        for image in img_list:
            try:
                img = cv.imread(f'{ROOT_DIR}/{inp_dir}/{image}',0)
                edges = cv.Canny(img,100,300)
                print(f"{ROOT_DIR}/{out_dir}/{image}")
                cv.imwrite(f"{ROOT_DIR}/{out_dir}/{image}", edges)
            except:
                continue