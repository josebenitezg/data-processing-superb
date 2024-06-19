import json
import cv2
import numpy as np
from torch import Tensor
from config_vars import *
import torchvision.transforms as T


def load_json(kp_det_filepath: str) -> dict:
    with open(kp_det_filepath, 'r') as f:
        kp_detections = json.load(f)
    
    return kp_detections


def tensor2image(tensor):
    nimg = tensor[0].permute(1, 2, 0) * 255
    nimg = nimg.cpu().numpy().astype(np.uint8)
    nimg = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
    
    return nimg


def spb2xyxy(x):
    # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = [0, 0, 0, 0]
    y[0] = int(x[0])  # top left x
    y[1] = int(x[1])  # top left y
    y[2] = int(x[0] + x[2])  # bottom right x
    y[3] = int(x[1] + x[3])  # bottom right y
    return y


def xyxy2xywhn(x, w=640, h=448):
    y = [0, 0, 0, 0]
    y[0] = ((x[0] + x[2]) / 2) / w  # x center
    y[1] = ((x[1] + x[3]) / 2) / h  # y center
    y[2] = (x[2] - x[0]) / w  # width
    y[3] = (x[3] - x[1]) / h  # height

    return y