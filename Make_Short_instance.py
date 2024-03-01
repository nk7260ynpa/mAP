import utils
import random
import argparse

random.seed(1048596)

def remove_images(gt, images_num_list) -> None:
    gt_images = []
    for img_info in gt["images"]:
        if img_info["id"] in images_num_list:
            gt_images.append(img_info)
    gt["images"] = gt_images
    return gt

def remove_annotations(gt, images_num_list) -> None:
    gt_annotations = []
    for ann in gt["annotations"]:
        if ann["image_id"] in images_num_list:
            ann['segmentation'] = []
            gt_annotations.append(ann)
    gt["annotations"] = gt_annotations
    return gt

def parse_args():
    parser = argparse.ArgumentParser(description='Make Short COCO Instance')
    parser.add_argument('--input', help='input json file', default='annotations/instances_val2014.json')
    parser.add_argument('--output', help='output json file', default='annotations/Short_instances.json')
    return parser.parse_args()

def main(opt) -> None:
    gt = utils.load_json(opt.input)
    # the 3 images are few annotations
    images_num_list = [147293, 141108, 323202]
    gt = remove_images(gt, images_num_list)
    gt = remove_annotations(gt, images_num_list)

    utils.save_json(gt, opt.output)

if __name__ == '__main__':
    opt = parse_args()
    main(opt)

