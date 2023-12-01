import os

def get_icon_path_from_name(icon_name):
    icon_path = __file__.replace("Icons.py", "Resource/Icons/") + icon_name
    if os.path.isfile(icon_path):
        return icon_path
    return False