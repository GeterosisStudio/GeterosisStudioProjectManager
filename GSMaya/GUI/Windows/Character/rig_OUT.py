#set ILLUSION chars transfer OUT
import maya.cmds as cmds

t_rig = [u'TransferRig:General', u'TransferRig:MainOffset', u'TransferRig:FootIKLoc_R', u'TransferRig:FootIKLoc_L', u'TransferRig:FootVectorLocIK_R', u'TransferRig:FootVectorLocIK_L', u'TransferRig:TorsoLoc',
u'TransferRig:TorsrHips', u'TransferRig:Spine1Loc',u'TransferRig:Spine2Loc', u'TransferRig:Spine3Loc', u'TransferRig:Neck1Loc', u'TransferRig:Neck2Loc',u'TransferRig:HeadLoc', u'TransferRig:HandVectorLoc_R',
u'TransferRig:HandIKLoc_R', u'TransferRig:HandVectorLoc_L', u'TransferRig:HandIKLoc_L', u'TransferRig:Pinky1Loc_R', u'TransferRig:Pinky2Loc_R', u'TransferRig:Pinky3Loc_R',
u'TransferRig:Ring1Loc_R', u'TransferRig:Ring2Loc_R', u'TransferRig:Ring3Loc_R', u'TransferRig:Middle1Loc_R', u'TransferRig:Middle2Loc_R', u'TransferRig:Middle3Loc_R', u'TransferRig:Index1Loc_R', u'TransferRig:Index2Loc_R',
u'TransferRig:Index3Loc_R', u'TransferRig:Thumb1Loc_R', u'TransferRig:Thumb2Loc_R', u'TransferRig:Thumb3Loc_R', u'TransferRig:Pinky1Loc_L', u'TransferRig:Pinky2Loc_L', u'TransferRig:Pinky3Loc_L', u'TransferRig:Ring1Loc_L',
u'TransferRig:Ring2Loc_L', u'TransferRig:Ring3Loc_L', u'TransferRig:Middle1Loc_L', u'TransferRig:Middle2Loc_L', u'TransferRig:Middle3Loc_L', u'TransferRig:Index1Loc_L', u'TransferRig:Index2Loc_L', u'TransferRig:Index3Loc_L',
u'TransferRig:Thumb1Loc_L', u'TransferRig:Thumb2Loc_L', u'TransferRig:Thumb3Loc_L']

roots = [u'General', u'Main']
foots = [u'IKLeg_R', u'IKLeg_L', u'PoleLeg_R', u'PoleLeg_L']
body =  [u'RootX_M', u'HipSwinger_M', u'FKSpine2_M', u'FKSpine4_M', u'FKChest_M', u'FKNeck_M', u'FKNeck1_M', u'FKHead_M']
arms = [u'Elbow_R', u'Wrist_R', u'Elbow_L', u'Wrist_L']
r_arm = [u'FKPinkyFinger1_R', u'FKPinkyFinger2_R', u'FKPinkyFinger3_R', u'FKRingFinger1_R', u'FKRingFinger2_R', u'FKRingFinger3_R', u'FKMiddleFinger1_R', u'FKMiddleFinger2_R', u'FKMiddleFinger3_R', u'FKIndexFinger1_R', u'FKIndexFinger2_R', u'FKIndexFinger3_R', u'FKThumbFinger1_R', u'FKThumbFinger2_R', u'FKThumbFinger3_R']
l_arm = [u'FKPinkyFinger1_L', u'FKPinkyFinger2_L', u'FKPinkyFinger3_L', u'FKRingFinger1_L', u'FKRingFinger2_L', u'FKRingFinger3_L', u'FKMiddleFinger1_L', u'FKMiddleFinger2_L', u'FKMiddleFinger3_L', u'FKIndexFinger1_L', u'FKIndexFinger2_L', u'FKIndexFinger3_L', u'FKThumbFinger1_L', u'FKThumbFinger2_L', u'FKThumbFinger3_L']
all_rig = roots + foots + body + arms + r_arm + l_arm

connections = ["TransferRig:FootIKLoc_R.Ball_Lean", "TransferRig:FootIKLoc_R.Ball_Rise", "TransferRig:FootIKLoc_R.Ball_Twist", "TransferRig:FootIKLoc_R.Fingers_Bend", "TransferRig:FootIKLoc_R.Heel_Rise", "TransferRig:FootIKLoc_R.Heel_Twist", "TransferRig:FootIKLoc_R.Roll", "TransferRig:FootIKLoc_R.Side", "TransferRig:FootIKLoc_R.Toe_Rise", "TransferRig:FootIKLoc_R.Toe_Twist", "TransferRig:FootIKLoc_L.Ball_Lean", "TransferRig:FootIKLoc_L.Ball_Rise", "TransferRig:FootIKLoc_L.Ball_Twist", "TransferRig:FootIKLoc_L.Fingers_Bend", "TransferRig:FootIKLoc_L.Heel_Rise", "TransferRig:FootIKLoc_L.Heel_Twist", "TransferRig:FootIKLoc_L.Roll", "TransferRig:FootIKLoc_L.Side", "TransferRig:FootIKLoc_L.Toe_Rise", "TransferRig:FootIKLoc_L.Toe_Twist"]
connectors= ["RollToes_R.rotateX", "r_footIk_CT.ballTwist", "IKToes_R.rotateZ", "r_footIk_CT.FingersBend", "RollHeel_R.rotateX", "RollHeel_R.rotateY", "RollToesEnd_R.rotateX", "IKLeg_R.rock", "r_footIk_CT.toeRise", "RollToesEnd_R.rotateY", "RollToes_L.rotateX", "l_footIk_CT.ballTwist", "IKToes_L.rotateZ", "l_footIk_CT.FingersBend", "RollHeel_L.rotateX", "RollHeel_L.rotateY", "RollToesEnd_L.rotateX", "IKLeg_L.rock", "l_footIk_CT.toeRise", "RollToesEnd_L.rotateY"]

def check_ctrl():
    returned = []
    for i in range(len(t_rig)):
        try:
            print t_rig[i], "  --->  ", all_rig[i]
        except:
            print "ERROR:", all_rig[i], "NOT DEFINED"
            returned += all_rig[i]
    return returned


def constrainting():
    for i in range(len(t_rig)):
        
        try:
            cmds.parentConstraint(all_rig[i], t_rig[i], mo = True, weight = 1)
        except:
            print "NOT CONSTRAINTING:", all_rig[i], t_rig[i]


def connect_attr(connector, connected):
    not_connected = []
    for i in range(len(connector)):
        try:
            cmds.connectAttr(connector[i], connected[i], f = True)
        except:
            not_connected.append(connected[i])
    if not_connected != []:
        print "!!!CHANNELS NOT CONNECTED!!!", not_connected
    else:
        print "ALL CHANNELS CONNECTED"





check_ctrl()
constrainting()
connect_attr(connectors, connections)






