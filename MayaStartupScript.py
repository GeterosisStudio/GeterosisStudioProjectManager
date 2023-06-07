import os
import sys

def maya_startup():
    full_path = os.path.realpath(__file__)
    dirname = os.path.dirname(full_path)

    Geterosis_Maya_PROJECT_PATH = dirname

    if Geterosis_Maya_PROJECT_PATH in sys.path:
        print("GSMaya path exist")
    else:
        sys.path.append(Geterosis_Maya_PROJECT_PATH)
        print("GSMaya path pasted")


"""
import sys
sys.path.insert(1, 'E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/')
import MayaStartupScript
reload(MayaStartupScript)
MayaStartupScript.maya_startup()
"""