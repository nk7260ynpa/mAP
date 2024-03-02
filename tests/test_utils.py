import utils

def test_intersection_cal():
    bbox1 = [10, 50, 100, 150]
    bbox2 = [60, 100, 150, 200]
    assert utils.intersection_cal(bbox1, bbox2) == 2000

def test_union_cal():
    bbox1 = [10, 50, 100, 150]
    bbox2 = [60, 100, 150, 200]
    assert utils.union_cal(bbox1, bbox2) == 16000

    