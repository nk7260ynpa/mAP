import utils

def test_intersection_cal():
    bbox1 = [10, 50, 100, 150]
    bbox2 = [60, 100, 150, 200]
    assert utils.intersection_cal(bbox1, bbox2) == 2000
    
    bbox1 = [10, 50, 100, 150]
    bbox2 = [120, 160, 150, 200]
    assert utils.intersection_cal(bbox1, bbox2) == 0

def test_union_cal():
    bbox1 = [10, 50, 100, 150]
    bbox2 = [60, 100, 150, 200]
    assert utils.union_cal(bbox1, bbox2) == 16000
    
    bbox1 = [10, 50, 100, 150]
    bbox2 = [120, 160, 150, 200]
    assert utils.intersection_cal(bbox1, bbox2) == 0

def test_iou_cal():
    bbox1 = [10, 50, 100, 150]
    bbox2 = [60, 100, 150, 200]
    assert round(utils.iou_cal(bbox1, bbox2), 3) == 0.125
    
    bbox1 = [10, 50, 100, 150]
    bbox2 = [120, 160, 150, 200]
    assert utils.intersection_cal(bbox1, bbox2) == 0

def test_xywh_to_xyxy():
    bbox = [10, 50, 100, 150]
    assert utils.xywh_to_xyxy(bbox) == [10, 50, 110, 200]

def test_gen_fake_bbox():
    for i in range(100):
        bbox = [10, 50, 100, 150]
        fake_bbox = utils.gen_fake_bbox(bbox)
        assert utils.iou_cal(bbox, fake_bbox) > 0.5

