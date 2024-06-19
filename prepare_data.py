import os
from config_vars import *
import download_labels as dl
import download_images as di
import convert_labels as cl


if __name__ == "__main__":
    for dir in DATA_DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)
    print("Dirs created.")

    print("Downloading labels...")
    dl.download_labels(LABELS_LINKS, DATA_PATH)
    dl.extract_labels(LABELS_LINKS, DATA_PATH)
    dl.delete_zips(LABELS_LINKS, DATA_PATH)
    print("Finished downloading labels.")
    
    print("Converting labels to YOLO format...")
    cl.create_yolo_labels(DATA_PATH, CLASSES)
    print("Finished conversion.")

    print("Downloading images from Superb...")
    di.download_images(METADATA_PATH)
    print("Finished downloading images.")

    
    

        