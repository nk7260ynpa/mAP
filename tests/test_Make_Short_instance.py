import Make_Short_instance


def test_remove_images():
    gt = {"images": [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]}
    images_num_list = [1, 2, 3]
    result = Make_Short_instance.remove_images(gt, images_num_list)
    assert result == {"images": [{"id": 1}, {"id": 2}, {"id": 3}]}


def test_remove_annotations():
    gt = {"annotations": [{"image_id": 1, "segmentation": [33.5, 22.4, 22.13, 12.67]}, 
                          {"image_id": 2, "segmentation": [33.5, 22.4, 22.13, 12.67]}, 
                          {"image_id": 3, "segmentation": [33.5, 22.4, 22.17, 12.67]}, 
                          {"image_id": 4, "segmentation": [33.5, 22.2, 22.13, 10.67]}, 
                          {"image_id": 5, "segmentation": [33.4, 22.4, 29.13, 12.67]}]}
    images_num_list = [1, 2, 3]
    result = Make_Short_instance.remove_annotations(gt, images_num_list)
    assert result == {"annotations": [{"image_id": 1, "segmentation":[]}, 
                                      {"image_id": 2, "segmentation":[]}, 
                                      {"image_id": 3, "segmentation":[]}]}

