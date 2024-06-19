import os
import json
from config_vars import *
import multiprocessing
import spb.sdk


def download_img(img_id: str) -> None:
    handler = SPB_CLIENT.get_data(img_id)
    img_name = handler.get_key()
    img_filepath = os.path.join(IMAGES_PATH, img_name)
    handler.download_image(img_filepath)
    return img_name


def parallel_task(file_name: str) -> None:
    meta_filepath = os.path.join(METADATA_PATH, file_name)
    with open(meta_filepath, 'r') as f:
        label_metadata = json.load(f)
    img_id = label_metadata['label_id']
    img_name = download_img(img_id)
    print(f'{img_name} downloaded', flush=True)


def download_images(metadata_path: str) -> None:
    """
    Create a list with the image files' names in the metadata_path dir.
    """
    meta_files  = os.listdir(metadata_path)
    # create a process pool that uses all cpus
    with multiprocessing.Pool(4) as pool:
    # call the function for each item in parallel
        pool.map(parallel_task, meta_files)

    
