import os
from config_vars import *
import download_images as di
import convert_labels as cl

if __name__ == "__main__":
    for dir in DATA_DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)
    print("Dirs created.")

    print("Converting labels to YOLO format...")
    cl.create_yolo_labels(DATA_PATH, CLASSES)
    print("Finished conversion.")

    print("Downloading images from Superb...")
    di.download_images(METADATA_PATH)
    print("Finished downloading images.")
