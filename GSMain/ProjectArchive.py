import zipfile
import os
import json
import subprocess


def archive_folder_winrar(folder_path, output_dir, archive_name, password):
    # create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # get config
    config_file = "../Settings/Config.json"
    with open(config_file) as f:
        config = json.load(f)
        winrar_path = config["WinRAR"]

    # create the archive with WinRAR and split it into parts
    archive_path = os.path.join(output_dir, archive_name + ".rar")
    cmd = '"{0}" a -ep1 -hp{1} -v2048000 "{2}" "{3}"'.format(winrar_path, password, archive_path, folder_path)
    subprocess.run(cmd, shell=True)

    return archive_path



