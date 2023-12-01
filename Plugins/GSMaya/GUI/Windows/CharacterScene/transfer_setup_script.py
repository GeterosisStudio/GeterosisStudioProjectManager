#set ILLUSION transfer rig transforms

import maya.cmds as cmds

body_head = [u'MH_rig_B_F:RootX_M', u'MH_rig_B_F:HipSwinger_M', u'MH_rig_B_F:FKSpine2_M', u'MH_rig_B_F:FKSpine4_M', u'MH_rig_B_F:FKChest_M', u'MH_rig_B_F:FKNeck_M', u'MH_rig_B_F:FKNeck1_M', u'MH_rig_B_F:FKHead_M']

foot = [u'MH_rig_B_F:IKLeg_R', u'MH_rig_B_F:PoleLeg_R']

arm = [u'MH_rig_B_F:FKScapula_R', u'MH_rig_B_F:FKShoulder_R', u'MH_rig_B_F:FKElbow_R', u'MH_rig_B_F:FKWrist_R']

hand = [u'MH_rig_B_F:FKPinkyFinger1_R', u'MH_rig_B_F:FKPinkyFinger2_R', u'MH_rig_B_F:FKPinkyFinger3_R', u'MH_rig_B_F:FKRingFinger1_R', u'MH_rig_B_F:FKRingFinger2_R', u'MH_rig_B_F:FKRingFinger3_R', u'MH_rig_B_F:FKMiddleFinger1_R', u'MH_rig_B_F:FKMiddleFinger2_R', u'MH_rig_B_F:FKMiddleFinger3_R', u'MH_rig_B_F:FKIndexFinger1_R', u'MH_rig_B_F:FKIndexFinger2_R', u'MH_rig_B_F:FKIndexFinger3_R', u'MH_rig_B_F:FKThumbFinger1_R', u'MH_rig_B_F:FKThumbFinger2_R', u'MH_rig_B_F:FKThumbFinger3_R']

right = [u'TransferRig:ClavicleLoc_R', u'TransferRig:HandVectorLoc_R', u'TransferRig:Shoulder_R', u'TransferRig:HandIKOffset_R', u'TransferRig:HandIKTrans_R', u'TransferRig:HandIKLoc_R', u'TransferRig:Index1Trans_R', u'TransferRig:Index1Loc_R', u'TransferRig:Index2Trans_R', u'TransferRig:Index2Loc_R', u'TransferRig:Index3Trans_R', u'TransferRig:Index3Loc_R', u'TransferRig:Middle1Trans_R', u'TransferRig:Middle1Loc_R', u'TransferRig:Middle2Trans_R', u'TransferRig:Middle2Loc_R', u'TransferRig:Middle3Trans_R', u'TransferRig:Middle3Loc_R', u'TransferRig:Ring1Trans_R', u'TransferRig:Ring1Loc_R', u'TransferRig:Ring2Trans_R', u'TransferRig:Ring2Loc_R', u'TransferRig:Ring3Trans_R', u'TransferRig:Ring3Loc_R', u'TransferRig:Pinky1Trans_R', u'TransferRig:Pinky1Loc_R', u'TransferRig:Pinky2Trans_R', u'TransferRig:Pinky2Loc_R', u'TransferRig:Pinky3Trans_R', u'TransferRig:Pinky3Loc_R', u'TransferRig:Thumb1Offset_R', u'TransferRig:Thumb1Trans_R', u'TransferRig:Thumb1Trans2_R', u'TransferRig:Thumb1Loc_R', u'TransferRig:Thumb2Trans_R', u'TransferRig:Thumb2Loc_R', u'TransferRig:Thumb3Trans_R', u'TransferRig:Thumb3Loc_R', u'TransferRig:FootIKTrans_R', u'TransferRig:FootIKLoc_R', u'TransferRig:FootVectorTransIK_R', u'TransferRig:FootVectorLocIK_R']

cmds.pointConstraint(body_head[0], "TransferRig:TorsoTrans", weight = 1)

#root scale
get_scale = cmds.getAttr("TransferRig:TorsoTrans" + ".translateY")
cmds.delete("TorsoTrans_pointConstraint1")
cmds.setAttr("TransferRig:root.scaleX", get_scale)
cmds.setAttr("TransferRig:root.scaleY", get_scale)
cmds.setAttr("TransferRig:root.scaleZ", get_scale)
cmds.setAttr("TransferRig:TorsoTrans.translateZ", 0)
cmds.setAttr("TransferRig:TorsoTrans.translateX", 0)
cmds.setAttr("TransferRig:TorsoTrans.translateY", 1)

#torso trans
cmds.pointConstraint(body_head[0], "TransferRig:TorsoTrans", weight = 1)
get_trans = cmds.getAttr("TransferRig:TorsoTrans" + ".translateZ")
cmds.delete("TorsoTrans_pointConstraint1")
cmds.setAttr("TransferRig:TorsoTrans.translateZ", get_trans)

#hip trans
cmds.pointConstraint(body_head[1], "TransferRig:TorsrHipsTrans", weight = 1)
get_scale = cmds.getAttr("TransferRig:TorsrHipsTrans" + ".translateY")
cmds.delete("TorsrHipsTrans_pointConstraint1")


#spine1 trans
cmds.pointConstraint(body_head[2], "TransferRig:Spine1Trans", weight = 1)
get_scale = cmds.getAttr("TransferRig:Spine1Trans" + ".translateY") * 2
cmds.delete("Spine1Trans_pointConstraint1")
cmds.setAttr("TransferRig:Spine1Offset.scaleX", get_scale)
cmds.setAttr("TransferRig:Spine1Offset.scaleY", get_scale)
cmds.setAttr("TransferRig:Spine1Offset.scaleZ", get_scale)

cmds.setAttr("TransferRig:Spine1Trans.translateX", 0)
cmds.setAttr("TransferRig:Spine1Trans.translateY", 0.5)
cmds.setAttr("TransferRig:Spine1Trans.translateZ", 0)

cmds.pointConstraint(body_head[2], "TransferRig:Spine1Trans", weight = 1)
cmds.delete("Spine1Trans_pointConstraint1")


#spine2 trans
cmds.pointConstraint(body_head[3], "TransferRig:Spine2Trans", weight = 1)
get_scale = cmds.getAttr("TransferRig:Spine2Trans" + ".translateY") * 2
cmds.delete("Spine2Trans_pointConstraint1")
cmds.setAttr("TransferRig:Spine2Offset.scaleX", get_scale)
cmds.setAttr("TransferRig:Spine2Offset.scaleY", get_scale)
cmds.setAttr("TransferRig:Spine2Offset.scaleZ", get_scale)

cmds.setAttr("TransferRig:Spine2Trans.translateX", 0)
cmds.setAttr("TransferRig:Spine2Trans.translateY", 0.5)
cmds.setAttr("TransferRig:Spine2Trans.translateZ", 0)

cmds.pointConstraint(body_head[3], "TransferRig:Spine2Trans", weight = 1)
cmds.delete("Spine2Trans_pointConstraint1")


#spine3 trans
cmds.pointConstraint(body_head[4], "TransferRig:Spine3Trans", weight = 1)
get_scale = cmds.getAttr("TransferRig:Spine3Trans" + ".translateY") * 2
cmds.delete("Spine3Trans_pointConstraint1")
cmds.setAttr("TransferRig:Spine3Offset.scaleX", get_scale)
cmds.setAttr("TransferRig:Spine3Offset.scaleY", get_scale)
cmds.setAttr("TransferRig:Spine3Offset.scaleZ", get_scale)

cmds.setAttr("TransferRig:Spine3Trans.translateX", 0)
cmds.setAttr("TransferRig:Spine3Trans.translateY", 0.5)
cmds.setAttr("TransferRig:Spine3Trans.translateZ", 0)

cmds.pointConstraint(body_head[4], "TransferRig:Spine3Trans", weight = 1)
cmds.delete("Spine3Trans_pointConstraint1")


#Neck1 trans
cmds.pointConstraint(body_head[5], "TransferRig:Neck1Trans", weight = 1)
get_scale = cmds.getAttr("TransferRig:Neck1Trans" + ".translateY") * 2
cmds.delete("Neck1Trans_pointConstraint1")
cmds.setAttr("TransferRig:Neck1Offset.scaleX", get_scale)
cmds.setAttr("TransferRig:Neck1Offset.scaleY", get_scale)
cmds.setAttr("TransferRig:Neck1Offset.scaleZ", get_scale)

cmds.setAttr("TransferRig:Neck1Trans.translateX", 0)
cmds.setAttr("TransferRig:Neck1Trans.translateY", 0.5)
cmds.setAttr("TransferRig:Neck1Trans.translateZ", 0)

cmds.pointConstraint(body_head[5], "TransferRig:Neck1Trans", weight = 1)
cmds.delete("Neck1Trans_pointConstraint1")



#Neck2 trans
cmds.pointConstraint(body_head[6], "TransferRig:Neck2Trans", weight = 1)
get_scale = cmds.getAttr("TransferRig:Neck2Trans" + ".translateY") * 2
cmds.delete("Neck2Trans_pointConstraint1")
cmds.setAttr("TransferRig:Neck2Offset.scaleX", get_scale)
cmds.setAttr("TransferRig:Neck2Offset.scaleY", get_scale)
cmds.setAttr("TransferRig:Neck2Offset.scaleZ", get_scale)

cmds.setAttr("TransferRig:Neck2Trans.translateX", 0)
cmds.setAttr("TransferRig:Neck2Trans.translateY", 0.5)
cmds.setAttr("TransferRig:Neck2Trans.translateZ", 0)

cmds.pointConstraint(body_head[6], "TransferRig:Neck2Trans", weight = 1)
cmds.delete("Neck2Trans_pointConstraint1")


#Head trans
cmds.pointConstraint(body_head[7], "TransferRig:HeadTrans", weight = 1)
get_scale = cmds.getAttr("TransferRig:HeadTrans" + ".translateY") * 2
cmds.delete("HeadTrans_pointConstraint1")
cmds.setAttr("TransferRig:HeadOffset.scaleX", get_scale)
cmds.setAttr("TransferRig:HeadOffset.scaleY", get_scale)
cmds.setAttr("TransferRig:HeadOffset.scaleZ", get_scale)

cmds.setAttr("TransferRig:HeadTrans.translateX", 0)
cmds.setAttr("TransferRig:HeadTrans.translateY", 0.5)
cmds.setAttr("TransferRig:HeadTrans.translateZ", 0)

cmds.pointConstraint(body_head[7], "TransferRig:HeadTrans", weight = 1)
cmds.delete("HeadTrans_pointConstraint1")


#foot trans
cmds.pointConstraint(foot[0], "TransferRig:FootIKTrans_R", weight = 1)
cmds.delete("FootIKTrans_R_pointConstraint1")


#Clavicle trans
cmds.pointConstraint(arm[0], "TransferRig:ClavicleTrans_R", weight = 1)
cmds.delete("ClavicleTrans_R_pointConstraint1")


#shoulder trans
cmds.pointConstraint(arm[1], "TransferRig:Shoulder_R", weight = 1)
cmds.delete("Shoulder_R_pointConstraint1")


#hand trans

cmds.pointConstraint(arm[3], "TransferRig:HandIKTrans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:HandIKTrans_R" + ".translateX") / 2.5
cmds.delete("HandIKTrans_R_pointConstraint1")
cmds.setAttr("TransferRig:HandIKOffset_R.scaleX", get_scale)
cmds.setAttr("TransferRig:HandIKOffset_R.scaleY", get_scale)
cmds.setAttr("TransferRig:HandIKOffset_R.scaleZ", get_scale)

cmds.setAttr("TransferRig:HandIKTrans_R.translateX", 2.5)
cmds.setAttr("TransferRig:HandIKTrans_R.translateY", 0)
cmds.setAttr("TransferRig:HandIKTrans_R.translateZ", 0)

cmds.pointConstraint(arm[3], "TransferRig:HandIKTrans_R", weight = 1)
cmds.delete("HandIKTrans_R_pointConstraint1")


#Pinky1 trans
cmds.pointConstraint(hand[0], "TransferRig:Pinky1Trans_R", weight = 1)
cmds.delete("Pinky1Trans_R_pointConstraint1")
cmds.aimConstraint(hand[1], "TransferRig:Pinky1Loc_R", skip="x")
cmds.delete("Pinky1Loc_R_aimConstraint1")

cmds.pointConstraint(hand[1], "TransferRig:Pinky2Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Pinky2Trans_R.translateX") * 2
cmds.delete("Pinky2Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Pinky1Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Pinky1Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Pinky1Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Pinky2Trans_R.translateX", 0.5)




#Pinky2 trans
cmds.pointConstraint(hand[1], "TransferRig:Pinky2Trans_R", weight = 1)
cmds.delete("Pinky2Trans_R_pointConstraint1")
cmds.aimConstraint(hand[2], "TransferRig:Pinky2Loc_R", skip="x")
cmds.delete("Pinky2Loc_R_aimConstraint1")

cmds.pointConstraint(hand[2], "TransferRig:Pinky3Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Pinky3Trans_R.translateX") * 2
cmds.delete("Pinky3Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Pinky2Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Pinky2Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Pinky2Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Pinky3Trans_R.translateX", 0.5)


#Ring1 trans
cmds.pointConstraint(hand[3], "TransferRig:Ring1Trans_R", weight = 1)
cmds.delete("Ring1Trans_R_pointConstraint1")
cmds.aimConstraint(hand[4], "TransferRig:Ring1Loc_R", skip="x")
cmds.delete("Ring1Loc_R_aimConstraint1")

cmds.pointConstraint(hand[4], "TransferRig:Ring2Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Ring2Trans_R.translateX") * 2
cmds.delete("Ring2Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Ring1Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Ring1Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Ring1Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Ring2Trans_R.translateX", 0.5)




#Pinky2 trans
cmds.pointConstraint(hand[4], "TransferRig:Ring2Trans_R", weight = 1)
cmds.delete("Ring2Trans_R_pointConstraint1")
cmds.aimConstraint(hand[5], "TransferRig:Ring2Loc_R", skip="x")
cmds.delete("Ring2Loc_R_aimConstraint1")

cmds.pointConstraint(hand[5], "TransferRig:Ring3Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Ring3Trans_R.translateX") * 2
cmds.delete("Ring3Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Ring2Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Ring2Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Ring2Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Ring3Trans_R.translateX", 0.5)


#Middle1 trans
cmds.pointConstraint(hand[6], "TransferRig:Middle1Trans_R", weight = 1)
cmds.delete("Middle1Trans_R_pointConstraint1")
cmds.aimConstraint(hand[7], "TransferRig:Middle1Loc_R", skip="x")
cmds.delete("Middle1Loc_R_aimConstraint1")

cmds.pointConstraint(hand[7], "TransferRig:Middle2Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Middle2Trans_R.translateX") * 2
cmds.delete("Middle2Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Middle1Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Middle1Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Middle1Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Middle2Trans_R.translateX", 0.5)




#Middle2 trans
cmds.pointConstraint(hand[7], "TransferRig:Middle2Trans_R", weight = 1)
cmds.delete("Middle2Trans_R_pointConstraint1")
cmds.aimConstraint(hand[8], "TransferRig:Middle2Loc_R", skip="x")
cmds.delete("Middle2Loc_R_aimConstraint1")

cmds.pointConstraint(hand[8], "TransferRig:Middle3Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Middle3Trans_R.translateX") * 2
cmds.delete("Middle3Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Middle2Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Middle2Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Middle2Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Middle3Trans_R.translateX", 0.5)


#Index1 trans
cmds.pointConstraint(hand[9], "TransferRig:Index1Trans_R", weight = 1)
cmds.delete("Index1Trans_R_pointConstraint1")
cmds.aimConstraint(hand[10], "TransferRig:Index1Loc_R", skip="x")
cmds.delete("Index1Loc_R_aimConstraint1")

cmds.pointConstraint(hand[10], "TransferRig:Index2Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Index2Trans_R.translateX") * 2
cmds.delete("Index2Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Index1Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Index1Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Index1Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Index2Trans_R.translateX", 0.5)




#Index2 trans
cmds.pointConstraint(hand[10], "TransferRig:Index2Trans_R", weight = 1)
cmds.delete("Index2Trans_R_pointConstraint1")
cmds.aimConstraint(hand[11], "TransferRig:Index2Loc_R", skip="x")
cmds.delete("Index2Loc_R_aimConstraint1")

cmds.pointConstraint(hand[11], "TransferRig:Index3Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Index3Trans_R.translateX") * 2
cmds.delete("Index3Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Index2Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Index2Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Index2Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Index3Trans_R.translateX", 0.5)


#Thumb1 trans
cmds.pointConstraint(hand[12], "TransferRig:Thumb1Trans_R", weight = 1)
cmds.delete("Thumb1Trans_R_pointConstraint1")
cmds.aimConstraint(hand[13], "TransferRig:Thumb1Loc_R", skip="x")
cmds.delete("Thumb1Loc_R_aimConstraint1")

cmds.pointConstraint(hand[13], "TransferRig:Thumb2Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Thumb2Trans_R.translateX") * 2
cmds.delete("Thumb2Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Thumb1Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Thumb1Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Thumb1Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Thumb2Trans_R.translateX", 0.5)




#Thumb2 trans
cmds.pointConstraint(hand[13], "TransferRig:Thumb2Trans_R", weight = 1)
cmds.delete("Thumb2Trans_R_pointConstraint1")
cmds.aimConstraint(hand[14], "TransferRig:Thumb2Loc_R", skip="x")
cmds.delete("Thumb2Loc_R_aimConstraint1")

cmds.pointConstraint(hand[14], "TransferRig:Thumb3Trans_R", weight = 1)
get_scale = cmds.getAttr("TransferRig:Thumb3Trans_R.translateX") * 2
cmds.delete("Thumb3Trans_R_pointConstraint1")
cmds.setAttr("TransferRig:Thumb2Trans_R.scaleX", get_scale)
cmds.setAttr("TransferRig:Thumb2Trans_R.scaleY", get_scale)
cmds.setAttr("TransferRig:Thumb2Trans_R.scaleZ", get_scale)
cmds.setAttr("TransferRig:Thumb3Trans_R.translateX", 0.5)

cmds.pointConstraint(arm[2], "TransferRig:HandVectorLoc_R", offset=(0,0,0), skip="z", weight=1)
cmds.delete("HandVectorLoc_R_pointConstraint1")


for i in range(len(right)):
    left = str(right[i]).replace('_R', '_L')
    tx = cmds.getAttr(right[i] + ".translateX")
    ty = cmds.getAttr(right[i] + ".translateY")
    tz = cmds.getAttr(right[i] + ".translateZ")
    
    rx = cmds.getAttr(right[i] + ".rotateX")
    ry = cmds.getAttr(right[i] + ".rotateY")
    rz = cmds.getAttr(right[i] + ".rotateZ")
    
    sx = cmds.getAttr(right[i] + ".scaleX")
    sy = cmds.getAttr(right[i] + ".scaleY")
    sz = cmds.getAttr(right[i] + ".scaleZ")
    
    
    
    
    cmds.setAttr(left + ".translateX", tx)
    cmds.setAttr(left + ".translateY", ty)
    cmds.setAttr(left + ".translateZ", tz)
    
    cmds.setAttr(left + ".rotateX", rx)
    cmds.setAttr(left + ".rotateY", ry)
    cmds.setAttr(left + ".rotateZ", rz)
    try:
        cmds.setAttr(left + ".scaleX", sx)
        cmds.setAttr(left + ".scaleY", sy)
        cmds.setAttr(left + ".scaleZ", sz)
    except:
        pass









