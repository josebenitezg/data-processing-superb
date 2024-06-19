import subprocess as sp
import os


def download_labels(links: dict, data_path: str):
    """
    Iterate over the links dict and download the files with the name of the key.
    """

    for file_name, link in links.items():
        file_path = os.path.join(data_path, file_name)
        args = [
            "wget",
            "-O",
            file_path,
            "{}".format(link),
        ]

        sp.call(args)


def extract_labels(links: dict, data_path: str):
    """
    Extract downloaded files.
    """
    for file_name, _ in links.items():
        file_path = os.path.join(data_path, file_name)
        args = [
            "unzip",
            "-q",
            "-o",
            file_path,
            "-d",
            data_path,
        ]

        sp.call(args)


def delete_zips(links: dict, data_path: str):
    """
    Delete remaining zips.
    """
    for file_name, _ in links.items():
        file_path = os.path.join(data_path, file_name)
        args = [
            "rm",
            file_path,
        ]

        sp.call(args)