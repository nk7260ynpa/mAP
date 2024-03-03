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

def test_gen_true_fake_bbox():
    for i in range(100):
        bbox = [10, 50, 100, 150]
        fake_bbox = utils.gen_true_fake_bbox(bbox, img_size=[110, 160])
        assert utils.iou_cal(bbox, fake_bbox) > 0.5
        assert fake_bbox[1] < fake_bbox[3]
        assert fake_bbox[0] >= 0
        assert fake_bbox[1] >= 0
        assert fake_bbox[2] <= 110
        assert fake_bbox[3] <= 160

    for i in range(100):
        bbox = [479.82, 328.63, 605.28, 442.09]
        fake_bbox = utils.gen_true_fake_bbox(bbox, img_size=[640, 512])
        assert utils.iou_cal(bbox, fake_bbox) > 0.5
        assert fake_bbox[1] < fake_bbox[3]
        assert fake_bbox[0] >= 0
        assert fake_bbox[1] >= 0
        assert fake_bbox[2] <= 640
        assert fake_bbox[3] <= 512
    

    

def test_gen_random_fake_bbox():
    for i in range(100):
        fake_bbox = utils.gen_random_fake_bbox(img_size=[110, 160])
        assert fake_bbox[0] < fake_bbox[2]
        assert fake_bbox[1] < fake_bbox[3]
        assert fake_bbox[0] >= 0
        assert fake_bbox[1] >= 0
        assert fake_bbox[2] <= 110
        assert fake_bbox[3] <= 160
    
    

def test_load_img_data():
    images_info = [
        {"id": 1, "file_name": "image1.jpg"},
        {"id": 2, "file_name": "image2.jpg"},
        {"id": 3, "file_name": "image3.jpg"},
    ]
    img_num = 1
    assert utils.load_img_data(images_info, img_num) == {"id": 1, "file_name": "image1.jpg"}
    
    img_num = 2
    assert utils.load_img_data(images_info, img_num) == {"id": 2, "file_name": "image2.jpg"}

    img_num = 3
    assert utils.load_img_data(images_info, img_num) == {"id": 3, "file_name": "image3.jpg"}


def test_load_ann_data():
    ann_info = [
        {"id": 1, "image_id": 1},
        {"id": 2, "image_id": 2},
        {"id": 3, "image_id": 3},
        {"id": 4, "image_id": 3}
    ]
    img_num = 1
    assert utils.load_ann_data(ann_info, img_num) == [
        {"id": 1, "image_id": 1}
    ]
    
    img_num = 2
    assert utils.load_ann_data(ann_info, img_num) == [
        {"id": 2, "image_id": 2}
    ]
    
    img_num = 3
    assert utils.load_ann_data(ann_info, img_num) == [
        {"id": 3, "image_id": 3}, {"id": 4, "image_id": 3}
    ]
    
    img_num = 4
    assert utils.load_ann_data(ann_info, img_num) == []

def test_decimal_2_bbox():
    bbox = [1.234, 2.345, 3.456, 4.567]
    assert utils.decimal_2_bbox(bbox) == [1.23, 2.35, 3.46, 4.57]

def test_gen_predict_label():
    image_id = 1
    category_id = 2
    bbox = [1.2313, 2.4123431, 3.24214, 4.242424]
    score = 0.5
    assert utils.gen_predict_label(image_id, category_id, bbox)["image_id"] == 1
    assert utils.gen_predict_label(image_id, category_id, bbox)["category_id"] == 2
    assert utils.gen_predict_label(image_id, category_id, bbox)["bbox"] == [1.23, 2.41, 3.24, 4.24]
    assert isinstance(utils.gen_predict_label(image_id, category_id, bbox)["score"], float)
    x = utils.gen_predict_label(image_id, category_id, bbox)["score"]
    assert (x - round(x, 3)) == 0

def test_liststr_to_listint():
    liststr = ["1", "2", "3", "4"]
    assert utils.liststr_to_listint(liststr) == [1, 2, 3, 4]
    
    liststr = ["1", "2", "3", "4", "5", "6", "7", "8"]
    assert utils.liststr_to_listint(liststr) == [1, 2, 3, 4, 5, 6, 7, 8]


    
