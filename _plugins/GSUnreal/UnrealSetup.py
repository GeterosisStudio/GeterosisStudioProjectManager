#insert this script into the startup script of the python project settings menu

import sys
GS_Unreal_PROJECT_PATH = "/"
GS_SITE_PACKAGES = GS_Unreal_PROJECT_PATH + "/venv/Lib/site-packages"


def add_system_path(path):
    if path in sys.path:
        pass
    else:
        sys.path.append(path)

add_system_path(GS_Unreal_PROJECT_PATH)
add_system_path(GS_SITE_PACKAGES)

try:
    from Plugins import GSUnreal as GU

    print("GSUnreal as GU Imported")
except:
    print("ERROR - GSUnreal NOT IMPORTED")
