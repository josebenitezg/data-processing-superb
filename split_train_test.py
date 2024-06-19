import os
import random
from config_vars import *


def symlink_crops(data_path: str) -> None:
    crops_path = os.path.join(data_path, "cropped_images")
    images_path = os.path.join(data_path, "images")
    crops_filenames = os.listdir(crops_path)
    for filename in crops_filenames:
        src = os.path.abspath(os.path.join(crops_path, filename))
        dst = os.path.join(images_path, filename)
        if not os.path.exists(dst):
            os.symlink(src, dst)


def get_img_trxid(img_name: str) -> str:
    """
    Get trx id from img name.
    """
    return img_name.split('_cam')[0]


def get_trx_ids(imgs_list: list) -> dict:
    """
    Returns all the trx ids present in the folder in a sorted list.
    """
    trx_ids = dict()
    for img in imgs_list:
        trx_id = img.split('_cam')[0]
        
        if trx_ids.get(trx_id, None):
            trx_ids[trx_id] += 1
        else:
            trx_ids[trx_id] = 1
    
    # Sort dict by values
    trx_ids = {k: v for k, v in sorted(trx_ids.items(), key=lambda item: item[1])}

    return trx_ids


def split_train_test(data_path: str, test_ratio: float, val_ratio: float) -> None:
    """Split the images in train, val and test subsets. The ratio for train subset
    will be 1-test_ratio-val_ratio.

    Args:
        data_path (str): data path.
        test_ratio (float): test/total_images ratio.
        val_ratio (float): val/total_images ratio.

    Returns:
        _type_: _description_
    """

    images_path = os.path.join(data_path, "images")
    image_filenames = os.listdir(images_path)

    trx_ids = get_trx_ids(image_filenames)        

    test_set_len = int(test_ratio * len(image_filenames))
    val_set_len = int(test_set_len + val_ratio * len(image_filenames))
    
    cumulative_sum = 0
    trx_ids_list = []
    test_flag = False
    val_flag = False
    
    for i, trx_id in enumerate(trx_ids.keys()):
        trx_ids_list.append(trx_id)  # Create list from dict keys
        cumulative_sum += trx_ids[trx_id]

        if cumulative_sum >= test_set_len and not test_flag:
            test_flag = True
            test_set_idx = i
        if cumulative_sum >= val_set_len and not val_flag:
            val_flag = True
            val_set_idx = i

    train_trx_ids = trx_ids_list[val_set_idx:]
    test_trx_ids = trx_ids_list[:test_set_idx]
    val_trx_ids = trx_ids_list[test_set_idx:val_set_idx]

    for img_filename in image_filenames:
        img_trx_id = get_img_trxid(img_filename)
        img_path = os.path.abspath(os.path.join(images_path, img_filename))
        img_iscrop = os.path.islink(img_path)

        if img_trx_id in train_trx_ids:
            with open(os.path.join(data_path, "train.txt"), "a") as f:
                f.write("{}\n".format(img_path))               

        if img_trx_id in test_trx_ids:
            with open(os.path.join(data_path, "test.txt"), "a") as f:
                f.write("{}\n".format(img_path))

        if img_trx_id in val_trx_ids:
            with open(os.path.join(data_path, "val.txt"), "a") as f:
                f.write("{}\n".format(img_path))


if __name__ == "__main__":
    # symlink_crops(DATA_PATH)
    split_train_test(DATA_PATH, test_ratio=0.125, val_ratio=0.125)