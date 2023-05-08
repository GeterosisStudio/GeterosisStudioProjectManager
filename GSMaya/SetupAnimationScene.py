# import maya.cmds as cmds
import json
import os
import shutil
from GSMain import Log, File
import maya.cmds as cmds


def export_targets(scene_path_file):

    settings_file = 'Settings/Libraries.json' # get libraries
    with open(settings_file) as f:
        source_char_variable_list = json.load(f)

    short_name = cmds.file(q=True, sceneName=True, shortName=True)
    scene_path_dirt = short_name = cmds.file(q=True, sceneName=True)
    if "/work/" in scene_path_root:
        scene_root_path_dirt = scene_path_dirt.replace("/work/", "/")
        scene_root_path = scene_root_path_dirt.replace(short_name, "")
    else:
        scene_root_path = scene_path_file.replace(short_name, "")
    target_scene_path = scene_root_path + "target/"
    target_list = str(scene_root_path) + "target.txt"   # get scene list(.txt)
    with open(target_list) as target:
        lines = [line.rstrip() for line in target]

    # Check target file for correctness
    target_checked = check_target_list(lines, source_char_variable_list)
    if target_checked != True:
        print(target_checked)
        return(False)

    for i in range(len(lines)):
        task = lines[i].split(", ")
        if len(task) == 1:  # if in line single string --> get char
            target_char = str(task[0])

        else: # source scene export
            source_proj = task[0]
            source_filename = task[1]
            source_char = task[2]
            source_anim_start = task[3]
            source_anim_end = task[4]
            target_anim_start = task[5]
            target_anim_end = task[6]
            source_scene_in_project = get_source_scene_path(source_proj, source_filename)
            if not source_scene_in_project:
                log = Log.warning("In project {0} Scene {1} not defined".format(source_proj, source_filename))
                print(source_char)
                print(log)
                continue
            source_scene_path = source_scene_in_project + source_filename
            new_char_file_name = source_char_variable_list["chars"][source_char]["file"]
            source_char_variables = source_char_variable_list
            source_char_var = source_char_variables["chars"][source_char]["name"]
            source_char_variables = source_char_variable_list
            source_char_ctrl = source_char_variables["chars"][source_char]["ct"]

            target_scene_run(source_scene_path, new_char_file_name, source_char_var, source_char_ctrl, source_anim_start, source_anim_end, target_char, target_anim_start, target_anim_end, target_scene_path)


def target_scene_run(source_scene_path, new_char_file_name, source_name_list, general_clrl, start_time, end_time, target_char,
                     target_anim_start, target_anim_end, target_scene_path):

    cmds.file(source_scene_path, o=True, f=True)
    source_active_char = None
    source_chars = source_name_list
    if cmds.objExists('chars_grp'):
        source_chars = cmds.listRelatives('chars_grp', c=True)
    else:
        # do reference node query
        pass
    for i in range(len(source_chars)):
        for k in range(len(source_name_list)):
            if not source_name_list[k] in str(source_chars[i]):
                continue
            else:
                source_active_char = str(source_chars[i])
    '''reload'''
    root_node = cmds.ls(source_active_char, rn=True)
    r_node = cmds.referenceQuery(root_node, rfn=True)
    ref = cmds.referenceQuery(r_node, f=True)
    this_char_file = cmds.referenceQuery(r_node, filename=True, shortName=True)
    ref_new = str(ref.replace(this_char_file, new_char_file_name))
    tr_out = cmds.file(ref_new, loadReference=r_node)
    '''vsrs'''
    source_active_char_root = ":" + source_active_char.split(":")[-1]
    namespace = source_active_char.replace(source_active_char_root, "")
    general_ct = namespace + ":" + general_clrl
    try:
        get_cam = cmds.listRelatives("cameras_grp")
    except:
        get_cam = cmds.ls(type="camera", transforms=True)
        try:
            get_cam.remove(u'perspShape')
            get_cam.remove(u'sideShape')
            get_cam.remove(u'topShape')
            get_cam.remove(u'frontShape')
        except:
            pass
    bake_objs = namespace + ":" + "TransferRig:root"
    transfer_exp_name = "source"
    '''vsrs'''
    loc_zero = cmds.spaceLocator()
    group = cmds.group(loc_zero)
    cmds.parentConstraint(general_ct, loc_zero, weight=1)
    cmds.pointConstraint(get_cam, group, weight=1)
    cmds.bakeResults(loc_zero, t=(start_time, end_time))
    cmds.delete(loc_zero[0] + "_parentConstraint1")
    cmds.parentConstraint(loc_zero, general_ct, weight=1)
    cmds.cutKey(get_cam)
    cmds.setAttr(get_cam[0] + ".translateX", 0)
    cmds.setAttr(get_cam[0] + ".translateY", 0)
    cmds.setAttr(get_cam[0] + ".translateZ", 0)
    cmds.setAttr(get_cam[0] + ".rotateX", 0)
    cmds.setAttr(get_cam[0] + ".rotateY", 0)
    cmds.setAttr(get_cam[0] + ".rotateZ", 0)
    transfer_exp = cmds.duplicate(bake_objs, name=transfer_exp_name, ic=True)
    cmds.parent(transfer_exp[0], w=True)
    cmds.select(transfer_exp[0])
    export_file = target_char + "_" + str(start_time) + "_" + str(end_time) + "_" + str(target_anim_start) + "_" + str(target_anim_end) +  ".ma"
    if not os.path.exists(target_scene_path):
        os.makedirs(target_scene_path)
    export_full_file_path = target_scene_path + export_file
    cmds.file(export_full_file_path, force=True, options = "v=0;", typ="mayaAscii", pr=True, es=True)

def get_source_scene_path(target_project=None, target_filename=None):
    target_scene_name = None
    if not target_project:
        log = Log.warning("Project{} not indicated".format(target_project))
        return target_project
    if not target_filename:
        log = Log.warning("Scene{} not indicated".format(target_filename))
        return target_filename
    else:
        with open('Settings/Libraries.json') as lib_settings_file:
            lib_settings = json.load(lib_settings_file)
        try:
            target_project_name = lib_settings["projects"][target_project]
        except:
            log = Log.warning("Project{} not defined".format(target_project))
            print(log)
            return None
        target_scene_name = target_project_name + target_filename + "_anm.ma"
        libs = lib_settings["libs"]
        for lib in libs:
            full_target_scene_path = lib_settings["libs"][lib] + target_scene_name
            if os.path.isfile(full_target_scene_path):
                return full_target_scene_path
    log = log = Log.warning(
        "In project {0} Scene {1} not defined, this path: {2}".format(target_project_name, target_filename,
                                                                      full_target_scene_path))


# TODO need testing
def check_target_list(target_lines, libraries_dict):
    log = {}
    for i in range(len(target_lines)):
        task = target_lines[i].split(", ")
        if len(task) == 1:
            k = i + 1
            task2 = target_lines[k].split(", ")
            if len(task2) > 1:
                continue
            else:
                log["Line " + str(i) + "," + str(k) + ":"] = "Two names in a row"
        elif len(task) != 6:
            log["Line " + str(i) + ":"] = "This string is wrong"
        else:

            # All Variables
            try:
                source_proj = task[0]
                source_filename = task[1]
                source_char = task[2]
                source_anim_start = task[3]
                source_anim_end = task[4]
                target_anim_start = task[5]
                target_anim_end = task[6]
            except Exception as e:
                Log.warning(e)

            # Check source project
            try:
                target_project_name = libraries_dict["projects"][target_project]
            except:
                log["Line " + str(i) + ":"] = "Project{} not defined".format(source_proj)
                continue

            # Check Scene exists
            target_scene_name = target_project_name + source_filename + ".mb"
            libs = lib_settings["libs"]
            scene_exsist = False
            for lib in libs:
                full_target_scene_path = lib_settings["libs"][lib] + target_scene_name
                if os.path.isfile(full_target_scene_path):
                    scene_exsist = True
                    break
            if scene_exsist != True:
                log["Line " + str(i) + ":"] =  "In project {0} Scene {1} not defined".format(target_project_name, source_filename + ".mb",)


            # Check Char exists
            try:
                source_char_variable_list["chars"][source_char]
            except:
                log["Line " + str(i) + ":"] = "Char {} not defoned".format(source_char)


            # Check source anim start is int
            try:
               check_is_int = int(source_anim_start)
            except:
                log["Line " + str(i) + ":"] = "Source animation start {} not int".format(source_anim_start)

            # Check source anim end is int
            try:
               check_is_int = int(source_anim_end)
            except:
                log["Line " + str(i) + ":"] = "Source animation end {} not int".format(source_anim_end)

            # Check target anim start is int
            try:
               check_is_int = int(target_anim_start)
            except:
                log["Line " + str(i) + ":"] = "Source animation end {} not int".format(target_anim_start)

            try:
               check_is_int = int(target_anim_end)
            except:
                log["Line " + str(i) + ":"] = "Source animation end {} not int".format(target_anim_end)

    if log:
        print(log)
        return False
    else:
        return True

def positioning_animation(source_time_start, source_time_end, target_start_time, target_end_time):
    cmds.select("persp")
    source_time_start = 0
    source_time_end = 29
    start_time = 0
    end_time = 50
    time_scale = start_time + end_time / source_time_start + source_time_end

    print(time_scale)
    cmds.scaleKey(time=(start_time, end_time), timeScale=time_scale, timePivot=start_time)


def scene_animation_setup():
    chars_grp = "chars_grp"
    chars = ""
    if cmds.objExists(chars_grp):
        chars = cmds.listRelatives(chars_grp)
    else:
        cmds.group(empty=True, name=chars_grp)
    if chars:
        print("yes")
    else:
        print("no")