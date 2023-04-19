import os

import cv2
import numpy as np
import random

from src.services.services_configs.base_services_cfgs import HooliGANConfig


class HoolGAN:
    def __init__(self, config: HooliGANConfig):
        self.path = config.ans_path_dir


    def generate(self):
        image = cv2.imread(self.path, cv2.IMREAD_COLOR)
        kernel = np.ones((30, 30), np.float32) / 900
        dst = cv2.filter2D(image, -1, kernel)
        return dst



if __name__ == '__main__':
    img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/services/hooligan_ans/1"
    config = HooliGANConfig(ans_path_dir=img_path)
    generator = HoolGAN(config)
    img = generator.generate()
    print(img)