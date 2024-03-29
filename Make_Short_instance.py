import utils
import argparse

def remove_images(gt, images_num_list) -> None:
    gt_images = []
    for img_info in gt["images"]:
        if str(img_info["id"]) in images_num_list:
            gt_images.append(img_info)
    gt["images"] = gt_images
    return gt

def remove_annotations(gt, images_num_list) -> None:
    gt_annotations = []
    for ann in gt["annotations"]:
        if str(ann["image_id"]) in images_num_list:
            ann['segmentation'] = []
            gt_annotations.append(ann)
    gt["annotations"] = gt_annotations
    return gt

def parse_args():
    parser = argparse.ArgumentParser(description='Make Short COCO Instance')
    parser.add_argument('--input', help='input json file', default='annotations/instances_val2014.json')
    parser.add_argument('--output', help='output json file', default='annotations/Short_instances.json')
    parser.add_argument('--img_num', help='images num list', default="147293, 141108, 323202")
    return parser.parse_args()

def main(opt) -> None:
    gt = utils.load_json(opt.input)
    # the 3 images are few annotations
    gt = remove_images(gt, opt.img_num.split(","))
    gt = remove_annotations(gt, opt.img_num.split(","))

    utils.save_json(gt, opt.output)

if __name__ == '__main__':
    opt = parse_args()
    main(opt)

