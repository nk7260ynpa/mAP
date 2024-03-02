import json

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
