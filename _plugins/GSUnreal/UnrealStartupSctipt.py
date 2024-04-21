import os
import sys


full_path = os.path.realpath(__file__)
dirname = os.path.dirname(full_path)

Geterosis_Unreal_PROJECT_PATH = dirname

if Geterosis_Unreal_PROJECT_PATH in sys.path:
    print("GSUnreal path exist")
else:
    sys.path.append(Geterosis_Unreal_PROJECT_PATH)
    print("GSUnreal path pasted")


