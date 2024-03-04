import utils
import random
import argparse

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_num_list', type=str, default="147293")
    parser.add_argument('--true_data', type=str, default="annotations/Short_instances.json")
    parser.add_argument('--fake_annotation_num', type=int, default=3)
    parser.add_argument('--save_path', type=str, default="annotations/xxxx.json")
    return parser.parse_args()

def gen_true_fake_predict(img_num_list, true_data):
    True_fake_ann_list = []
    for img_num in img_num_list:
        annotation_num_datas = utils.load_ann_data(true_data["annotations"], img_num)
        img_info = utils.load_img_data(true_data["images"], img_num)
        img_size = img_info["width"], img_info["height"]
        for annotation_num_data in annotation_num_datas:
            True_ann = annotation_num_data["bbox"]
            True_bbox = utils.xywh_to_xyxy(True_ann)
            True_fake_bbox = utils.gen_true_fake_bbox(True_bbox, img_size)
            True_fake_ann = utils.gen_predict_ann(img_num, 
                                                    annotation_num_data["category_id"], 
                                                    utils.xyxy_to_xywh(True_fake_bbox))
            True_fake_ann_list.append(True_fake_ann)
    return True_fake_ann_list

def gen_random_fake_predict(img_num_list, true_data, True_fake_ann_list, fake_annotation_num):
    for img_num in img_num_list:
        img_ann_list = []
        img_info = utils.load_img_data(true_data["images"], img_num)
        img_size = img_info["width"], img_info["height"]
        img_ann_list = img_ann_list + utils.load_ann_data(true_data["annotations"], img_num)
        img_ann_list = img_ann_list + utils.load_ann_data(True_fake_ann_list, img_num)
        
        for i in range(fake_annotation_num):
            while True:
                random_fake_ann = utils.gen_random_fake_bbox(img_size)
                random_fake_ann_pass = True
                for annotation in img_ann_list:
                    if utils.iou_cal(utils.xywh_to_xyxy(annotation["bbox"]), random_fake_ann) > 0.5:
                        random_fake_ann_pass = False
                if random_fake_ann_pass:
                    img_ann_list.append(
                        utils.gen_predict_ann(image_id=img_num,
                                                category_id=random.randint(0, 80),
                                                bbox=utils.xyxy_to_xywh(random_fake_ann))
                    )
                    break

    img_ann_list = [ann for ann in img_ann_list if ann not in utils.load_ann_data(true_data["annotations"], img_num)]
    return img_ann_list

def main(opt):
    img_num_list = opt.img_num_list
    true_data = utils.load_json(opt.true_data)
    fake_annotation_num = opt.fake_annotation_num

    img_num_list = img_num_list.split(",")
    img_num_list = utils.liststr_to_listint(img_num_list)
    True_fake_ann_list = gen_true_fake_predict(img_num_list, true_data)
    img_ann_list = gen_random_fake_predict(img_num_list, true_data, True_fake_ann_list, fake_annotation_num)
    utils.save_json(img_ann_list, opt.save_path)



if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
                            