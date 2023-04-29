
import sys

GS_DIR = "/GSMaya"


def run():
    if GS_DIR not in sys.path:
        sys.path.append(GS_DIR)


