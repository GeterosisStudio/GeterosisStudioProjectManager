import os

GSPM_MAYA_SCENE_CLS = None
GSPM_PATH = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/").replace("Settings", "")
print GSPM_PATH