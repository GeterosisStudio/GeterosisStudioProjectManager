import json
import pprint

import collections
all = ["General", "MainOffset", "TorsoLoc", "TorsrHips", "Spine1Loc", "Spine2Loc", "Spine3Loc", "Neck1Loc", "Neck2Loc",
       "HeadLoc", "FootIKLoc_R", "FootVectorLocIK_R", "Shoulder_R", "HandVectorLoc_R", "HandIKLoc_R", "Thumb1Loc_R",
       "Thumb2Loc_R", "Thumb3Loc_R", "Index1Loc_R", "Index2Loc_R", "Index3Loc_R", "Middle1Loc_R", "Middle2Loc_R", "Middle3Loc_R",
       "Ring1Loc_R", "Ring2Loc_R", "Ring3Loc_R", "Pinky1Loc_R", "Pinky2Loc_R", "Pinky3Loc_R"]

dict = collections.OrderedDict

for elem in all:
    dict[elem.replace("Loc", "")] = elem

with open("TransferRig.json", "w") as f:
    json.dump(dict, f, indent=4)