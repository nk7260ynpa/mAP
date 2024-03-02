import json
import random

def load_json(file, mode='r'):
    with open(file, mode) as f:
        return json.load(f)
    
def save_json(data, file, mode='w'):
    with open(file, mode) as f:
        json.dump(data, f, indent=4)

def intersection_cal(bbox1, bbox2):
    bbox1_x1, bbox1_y1, bbox1_x2, bbox1_y2 = bbox1
    bbox2_x1, bbox2_y1, bbox2_x2, bbox2_y2 = bbox2
    if (bbox1_x1 > bbox2_x2) | (bbox1_x2 < bbox2_x1) | (bbox1_y1 > bbox2_y2) | (bbox1_y2 < bbox2_y1):
        return 0
    else:
        x1 = max(bbox1_x1, bbox2_x1)
        y1 = max(bbox1_y1, bbox2_y1)
        x2 = min(bbox1_x2, bbox2_x2)
        y2 = min(bbox1_y2, bbox2_y2)
        return (x2 - x1) * (y2 - y1)

def union_cal(bbox1, bbox2):
    bbox1_x1, bbox1_y1, bbox1_x2, bbox1_y2 = bbox1
    bbox2_x1, bbox2_y1, bbox2_x2, bbox2_y2 = bbox2
    if (bbox1_x1 > bbox2_x2) | (bbox1_x2 < bbox2_x1) | (bbox1_y1 > bbox2_y2) | (bbox1_y2 < bbox2_y1):
        return 0
    else:
        bbox1_area = (bbox1_x2 - bbox1_x1) * (bbox1_y2 - bbox1_y1)
        bbox2_area = (bbox2_x2 - bbox2_x1) * (bbox2_y2 - bbox2_y1)
        return bbox1_area + bbox2_area - intersection_cal(bbox1, bbox2)
    
def iou_cal(bbox1, bbox2):
    return intersection_cal(bbox1, bbox2) / (union_cal(bbox1, bbox2)+0.00001)

def xywh_to_xyxy(bbox):
    x, y, w, h = bbox
    return [x, y, x + w, y + h]

def xyxy_to_xywh(bbox):
    x1, y1, x2, y2 = bbox
    return [x1, y1, x2 - x1, y2 - y1]

def gen_true_fake_bbox(bbox, img_size, AP_Level=0.5):
    x1, y1, x2, y2 = bbox
    w = x2 - x1
    h = y2 - y1
    while True:
        x1 = x1 + x1 * random.uniform(-0.2, 0.2)
        y1 = y1 + y1 * random.uniform(-0.2, 0.2)
        x2 = x2 + x2 * random.uniform(-0.2, 0.2)
        y2 = y2 + y2 * random.uniform(-0.2, 0.2)
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(img_size[0], x2)
        y2 = min(img_size[1], y2)
        if iou_cal(bbox, [x1, y1, x2, y2]) > AP_Level:
            break
    return [x1, y1, x2, y2]

def gen_random_fake_bbox(img_size):
    x1 = random.randint(0, img_size[0]-1)
    y1 = random.randint(0, img_size[1]-1)
    x2 = random.randint(x1+1, img_size[0])
    y2 = random.randint(y1+1, img_size[1])
    return [x1, y1, x2, y2]

def load_img_data(images_info, img_num):
    for image_info in images_info:
        if image_info["id"] == img_num:
            return image_info
        
def load_ann_data(ann_info, img_num):
    ann_list = []
    for ann in ann_info:
        if ann["image_id"] == img_num:
            ann_list.append(ann)
    return ann_list

