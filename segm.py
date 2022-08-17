import torch
from PIL import Image
import savings

def pic_segment():

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    im = Image.open(savings.segm_save())
    results = model(im)
    results.save(savings.ruin_send())