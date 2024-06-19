import os
import json
import helper_functions as hf
from tqdm import tqdm


def create_yolo_labels(data_dirpath: str, classes: dict):
    meta_dirpath = os.path.join(data_dirpath, "meta", "default_dataset")
    meta_files = os.listdir(meta_dirpath)

    for file_name in tqdm(meta_files):
        meta_filepath = os.path.join(meta_dirpath, file_name)
        
        with open(meta_filepath, 'r') as f:
            label_metadata = json.load(f)

        label_name = label_metadata['label_path'][0]
        img_name = label_metadata['data_key']
        img_width = label_metadata['image_info']['width']
        img_height = label_metadata['image_info']['height']
        im_size = [img_width, img_height]

        label_filepath = os.path.join(data_dirpath, label_name)

        with open(label_filepath, 'r') as f:
            label = json.load(f)
        if not label:
            continue


        lines = superb_2_yolo(label, im_size, classes)
        yololabel_name = "{}.txt".format(os.path.splitext(img_name)[0])
        yololabel_path = os.path.join(data_dirpath, "yolo_labels", yololabel_name)

        with open(yololabel_path, 'w') as f:
            for line in lines:
                f.write("{}\n".format(line))


def superb_2_yolo(label: dict, im_size: list, classes: dict) -> list:
    """Convert the JSON label exported from Superb to Yolo format
    saving it as a txt file.

    Args:
        label (dict): JSON label from Superb
        im_size (list): [w, h] size of img
        classes (dict): maps from cls name to cls number
    """
    objects = label['objects']
    lines = []

    for obj in objects:
        cls = classes.get(obj['class_name'], len(classes))
        coords = obj['annotation']['coord']
        box = [
            coords['x'],
            coords['y'],
            coords['width'],
            coords['height']
        ]
        box = hf.spb2xyxy(box)
        box = hf.xyxy2xywhn(box, im_size[0], im_size[1])

        line = "{:d} {:.6f} {:.6f} {:.6f} {:.6f}".format(
                cls, box[0], box[1], box[2], box[3])
        lines.append(line)
        del(line)

    return lines
