import maya.cmds as cmds
import os
import shutil


project_path = None
char_name = cmds.file(q=True, sceneName=True, shortName=True).split(".")[0].replace('_full_rig', '')
chars_dir = "assets/Chars/".format(project_path)
char_full_dir = chars_dir + char_name
char_full_dir_work = char_full_dir + "/work/"
old_file_dir = cmds.file(q=True, sceneName=True).replace(cmds.file(q=True, sceneName=True, shortName=True), "")


def generate_char():
    if not os.path.exists(char_full_dir_work):
        os.makedirs(char_full_dir_work)
        print "CHAR DIR CREATED:", chars_dir + char_name
    else:
        print "CHAR DIR EXIST:", chars_dir + char_name
    shutil.copyfile(old_file_dir + char_name + ".dna", char_full_dir + "/" + char_name + ".dna")
    shutil.copyfile(old_file_dir + char_name + "_rl.dna", char_full_dir + "/" + char_name + "_rl.dna")
    cmds.file(rename=char_full_dir_work + char_name + ".0001" + ".ma")
    cmds.file(s=True)

    rig_ident = {"m_srt_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_M.ma".format(project_path),
                 "f_srt_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_F_S.ma".format(project_path),
                 "f_srt_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_F_B.ma".format(project_path),
                 "m_med_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_M_S.ma".format(project_path),
                 "m_med_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_M_B.ma".format(project_path),
                 "m_med_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_M.ma".format(project_path),
                 "f_med_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_F.ma".format(project_path),
                 "f_med_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_F_S.ma".format(project_path),
                 "m_tal_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_M.ma".format(project_path),
                 "f_srt_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_F.ma".format(project_path),
                 "f_tal_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_F_B.ma".format(project_path),
                 "m_tal_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_M_S.ma".format(project_path),
                 "m_tal_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_M_B.ma".format(project_path),
                 "f_tal_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_F_S.ma".format(project_path),
                 "f_tal_nrw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_B_F.ma".format(project_path),
                 "f_med_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_M_F_B.ma".format(project_path),
                 "m_srt_ovw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_M_B.ma".format(project_path),
                 "m_srt_unw_body_lod0_mesh": "{}assets/Chars/1Defult/MH/rig/MH_rig_S_M_S.ma".format(project_path)}

    dhi = [u'DHIhead:clavicle_pec_r', u'DHIhead:spine_04_latissimus_r', u'DHIhead:upperarm_in_r',
           u'DHIhead:upperarm_fwd_r',
           u'DHIhead:upperarm_out_r', u'DHIhead:clavicle_out_r', u'DHIhead:clavicle_scap_r',
           u'DHIhead:upperarm_bck_r', u'DHIhead:upperarm_correctiveRoot_r', u'DHIhead:clavicle_r',
           u'DHIhead:spine_04_latissimus_l', u'DHIhead:clavicle_pec_l', u'DHIhead:upperarm_in_l',
           u'DHIhead:upperarm_fwd_l',
           u'DHIhead:upperarm_out_l', u'DHIhead:clavicle_scap_l', u'DHIhead:clavicle_out_l', u'DHIhead:upperarm_bck_l',
           u'DHIhead:upperarm_l', u'DHIhead:clavicle_l', u'DHIhead:upperarm_r',
           u'DHIhead:upperarm_correctiveRoot_l', u'DHIhead:head', u'DHIhead:neck_02', u'DHIhead:neck_01',
           u'DHIhead:spine_05', u'DHIhead:spine_04']

    dodelete_elems = [u'head_lod1_grp', u'head_lod2_grp', u'head_lod3_grp', u'head_lod4_grp', u'head_lod5_grp',
                      u'head_lod6_grp', u'head_lod7_grp', "body_grp", "Lights", "root_drv", "DHIbody:root",
                      "body_lod0_layer",
                      "head_lod0_layer", "head_lod1_layer", "head_lod2_layer", "head_lod3_layer", "head_lod4_layer",
                      "head_lod5_layer", "head_lod6_layer", "head_lod7_layer", "body_lod1_layer", "body_lod2_layer",
                      "body_lod3_layer"]

    # import rig
    mh_bodys = rig_ident.keys()
    cmds.rename("rig", "DHI_rig")
    for i in range(len(mh_bodys)):
        if cmds.objExists(mh_bodys[i]):
            cmds.file(rig_ident[mh_bodys[i]], r=True, namespace="rig")
            break

    # set attrs
    cmds.setAttr("CTRL_faceGUIfollowHead.translateY", 1)
    cmds.group(n="root_grp", em=True)
    cmds.parent("DHI_rig", "DHIhead:spine_04", "root_grp")
    cmds.setAttr("DHIhead:spine_04.visibility", 0)

    # delete non need elems

    cmds.delete(dodelete_elems)
    if cmds.objExists("export_geo_GRP"):
        cmds.delete("export_geo_GRP")

    # Offset head rig controls
    cmds.select("rig:DHIbody:spine_04", r=True)
    cmds.select("DHIhead:spine_04", add=True)
    cmds.parentConstraint(mo=False, weight=1)
    cmds.delete("spine_04_parentConstraint1")

    dhi_heads = [u'DHIhead:head', u'DHIhead:neck_02', u'DHIhead:neck_01']
    rig_offset = [u'rig:FKExtraHead_M', u'rig:FKExtraNeck1_M', u'rig:FKExtraNeck_M']

    for i in range(len(dhi_heads)):
        cmds.select(dhi_heads[i], r=True)
        cmds.select(rig_offset[i], add=True)
        cmds.pointConstraint(mo=False, weight=1)
    cmds.delete(u'FKExtraHead_M_pointConstraint1', u'FKExtraNeck1_M_pointConstraint1',
                u'FKExtraNeck_M_pointConstraint1')
    print "EXECUTE: Offset head rig controls"

    # constraint head to rig
    rig_prefix = "rig:DHIbody:"
    for i in range(len(dhi)):
        dhi_value = dhi[i].split(":")
        rig_value = rig_prefix + dhi_value[1]
        if not cmds.objExists(rig_value):
            print "NOT DEFINED:", rig_value
        else:
            try:
                cmds.select(rig_value, r=True)
                cmds.select(dhi[i], add=True)
                cmds.parentConstraint(mo=False, weight=1)
            except:
                print "NOT PARENT:", rig_value, "----->", dhi[i]
    print "EXECUTE: constraint head to rig"

    # parent rig in head root_grp

    cmds.parent("rig:root_grp", "root_grp")
    print "EXECUTE: parent rig in head root_grp"
    '''TODO. remove magic variables'''
    cmds.file(rename=char_full_dir_work + char_name + ".ma")
    cmds.file(s=True)
    cmds.file(rename=char_full_dir + "/" + char_name + ".ma")
    cmds.file(s=True)
    print "EXECUTE: Save final char file", char_full_dir + char_name + ".ma"


if __name__ == "__main__":
    generate_char()