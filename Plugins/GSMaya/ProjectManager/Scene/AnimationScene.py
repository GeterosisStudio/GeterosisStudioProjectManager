import maya.cmds as cmds
import maya.mel as mel
import os
import json

import AnimationBaseScene


class AnimationScene(AnimationBaseScene.AnimationBaseScene):


    def check_scene(self):
        shots = cmds.ls(type="shot")
        end_frames = []
        for shot in shots:
            end_frames.append(cmds.getAttr("{}.endFrame".format(shot)))

        scene_start_time = cmds.playbackOptions(ast=0)
        scene_end_time = cmds.playbackOptions(aet=max(end_frames))
        scene_start_slide = cmds.playbackOptions(min=0)
        scene_end_slide = cmds.playbackOptions(max=max(end_frames))
        fps = mel.eval('currentTimeUnitToFPS')
        check = True
        if fps != 30:
            print("FPS NOT EQUAL 30FPS")
            check = False
        return check

    def get_chars(self):
        chars = self.list_all_children("chars_grp")
        chars_names = []
        for i in range(len(chars)):
            chars_names.append(chars[i].replace(":root_grp", ""))
        return chars_names

    def check_sequence_correct(self):
        check = True
        start_frames = []
        end_frames = []
        shots = cmds.ls(type="shot")
        cmds.listConnections("sequencer1", type="shot")
        for shot in shots:
            shot_name = cmds.getAttr("{}.shotName".format(shot))  # Query shot's name.
            start_frame = cmds.getAttr("{}.startFrame".format(shot))  # Query shot's start frame.
            sequence_start_frame = cmds.getAttr(
                "{}.sequenceStartFrame".format(shot))  # Query shot's sequence start frame.
            sequence_end_frame = cmds.getAttr("{}.sequenceEndFrame".format(shot))  # Query shot's sequence start frame.
            end_frame = cmds.getAttr("{}.endFrame".format(shot))  # Query shot's end frame.
            shot_scale = cmds.getAttr("{}.scale".format(shot))
            camera = cmds.listConnections(shot, type="camera")

            if not camera:
                print("IN SHOT: {} NOT CAMERA CONNECTION".format(shot))
                check = False
            if start_frame != sequence_start_frame:
                print("IN SHOT: {} START FRAME NOT EQUAL SEQUENCE START FRAME".format(shot))
                check = False
            if end_frame != sequence_end_frame:
                print("IN SHOT: {} END FRAME NOT EQUAL SEQUENCE END FRAME".format(shot))
                check = False
            if shot_scale != 1:
                print("IN SHOT: {} SCALE NOT EQUAL 1".format(shot))
                check = False

            start_frames.append(start_frame)
            end_frames.append(end_frame)
        if not 0 in start_frames:
            print("THIS SCENE DOES NOT START FROM ZERO")
            check = False
        for i in range(len(shots)):
            if start_frames[i] != 0:
                if not start_frames[i] - 1 in end_frames:
                    print("SEQUENCE IS INCORRECT IN {}".format(shots[i]))
                    check = False
        return check

    def get_export_path(self):
        scene_path = cmds.file(q=True, sceneName=True)
        scene_name = cmds.file(q=True, sceneName=True, shortName=True)
        export_path = scene_path.replace(scene_name, "") + "export/"
        if "/work" in export_path:
            export_path = export_path.replace("/work", "")
        return export_path

    def export_cameras(self):
        cam_export_path = self.get_export_path() + "cameras/"
        shots = cmds.ls(type="shot")
        if os.path.exists(cam_export_path):
            pass
        else:
            os.makedirs(cam_export_path)
            print("DIR CREATED")
        print(cam_export_path)
        for shot in shots:
            camera = cmds.listConnections(shot, type="camera")

            if cmds.listConnections(camera, type="animCurve"):
                start_frame = cmds.getAttr("{}.startFrame".format(shot))
                end_frame = cmds.getAttr("{}.endFrame".format(shot))
                scene_start_slide = cmds.playbackOptions(min=start_frame)
                scene_end_slide = cmds.playbackOptions(max=end_frame)
                cmds.bakeResults(camera)
                cmds.keyTangent(cmds.listConnections(camera, type="animCurve"), itt="auto", ott="auto")
            try:
                cmds.parent(camera, w=True)
            except:
                pass
            cam_export_name = cam_export_path + str(camera[0]) + ".fbx"
            cam_curves = cmds.listConnections(camera, type="animCurve")
            if cam_curves:

                cam_curves.append(str(camera[0]))
                cmds.select(cam_curves)
                cmds.file(cam_export_name, force=True, options="v=0;", typ="FBX export", pr=True, es=True)
            else:
                cmds.select(camera)
                cmds.file(cam_export_name, force=True, options="v=0;", typ="FBX export", pr=True, es=True)

            cmds.parent(camera, "cameras_grp")

    def export_body(self, root_name):
        body_root = ("root")

        if cmds.objExists(body_root):
            cmds.delete(body_root)

        namespace = root_name.split(":")[0]
        char_export_path = self.get_export_path() + "chars/"
        char_export_name = char_export_path + str(namespace) + "_body" + ".fbx"
        body_ref = namespace + ":rig:DHIbody:root"
        body = cmds.duplicate(body_ref, ic=True)
        cmds.parent(body_root, w=True)
        cmds.setAttr(body_root + ".visibility", 1)
        cmds.bakeResults(body, simulation=True,
                         t=(int(cmds.playbackOptions(q=True, min=True)), int(cmds.playbackOptions(q=True, max=True))))
        anm_curves = cmds.listConnections(body, type="animCurve")
        cmds.filterCurve(anm_curves)
        cmds.select(body_root, r=True)
        cmds.select(anm_curves, add=True)
        cmds.file(char_export_name, force=True, options="v=0;", typ="FBX export", pr=True, es=True)
        cmds.delete(anm_curves, body_root)

    def export_face(self, root_name):
        namespace = root_name.split(":")[0]
        face_export_path = self.get_export_path() + "chars/"
        face_export_name = face_export_path + str(namespace) + "_face" + ".fbx"
        face_ref = [namespace + ":DHI_rig"]
        face_ref_geos = self.list_all_children(namespace + ":FacialControls")
        face_export = cmds.duplicate(face_ref, ic=True)
        cmds.parent(face_export[0], w=True)
        cmds.delete("geometry_grp")
        cmds.delete("rig_setup_grp")
        cmds.rename(face_export[0], "rig")
        face_export = "rig"

        bake_face = [u'CTRL_L_mouth_tightenD', u'CTRL_L_mouth_tightenU', u'CTRL_R_mouth_tightenU',
                     u'CTRL_R_mouth_tightenD',
                     u'CTRL_L_mouth_lipsPressU', u'CTRL_R_mouth_lipsPressU', u'CTRL_L_mouth_lipBiteU',
                     u'CTRL_R_mouth_lipBiteU', u'CTRL_R_mouth_lipsRollD', u'CTRL_L_mouth_lipsRollU',
                     u'CTRL_R_mouth_lipsRollU', u'CTRL_L_mouth_lipsRollD', u'CTRL_L_nose_nasolabialDeepen',
                     u'CTRL_R_nose_nasolabialDeepen', u'CTRL_L_eye_faceScrunch', u'CTRL_R_eye_faceScrunch',
                     u'CTRL_L_eyelashes_tweakerIn', u'CTRL_R_eyelashes_tweakerIn', u'CTRL_L_eyelashes_tweakerOut',
                     u'CTRL_R_eyelashes_tweakerOut', u'CTRL_R_mouth_cornerSharpnessD', u'CTRL_R_mouth_thicknessU',
                     u'CTRL_R_mouth_thicknessD', u'CTRL_L_mouth_cornerSharpnessD', u'CTRL_L_mouth_thicknessU',
                     u'CTRL_L_mouth_thicknessD', u'CTRL_L_mouth_lipsBlow', u'CTRL_R_mouth_lipsBlow', u'CTRL_C_eyesAim',
                     u'CTRL_R_eyeAim', u'CTRL_L_eyeAim', u'CTRL_R_mouth_pushPullU', u'CTRL_L_mouth_pushPullU',
                     u'CTRL_L_mouth_pushPullD', u'CTRL_R_mouth_pushPullD', u'CTRL_R_mouth_stickyOuterU',
                     u'CTRL_L_mouth_cornerSharpnessU', u'CTRL_R_mouth_cornerSharpnessU', u'CTRL_L_mouth_stickyOuterU',
                     u'CTRL_L_mouth_stickyInnerU', u'CTRL_R_mouth_stickyOuterD', u'CTRL_R_mouth_stickyInnerU',
                     u'CTRL_C_mouth_stickyU', u'CTRL_L_mouth_stickyInnerD', u'CTRL_R_mouth_stickyInnerD',
                     u'CTRL_C_mouth_stickyD', u'CTRL_L_mouth_lipSticky', u'CTRL_R_mouth_lipSticky',
                     u'CTRL_L_mouth_stickyOuterD', u'CTRL_C_tongue', u'CTRL_C_tongue_roll', u'CTRL_C_tongue_narrowWide',
                     u'CTRL_C_tongue_inOut', u'CTRL_C_tongue_tip', u'CTRL_C_tongue_press', u'CTRL_L_jaw_ChinRaiseU',
                     u'CTRL_R_jaw_ChinRaiseU', u'CTRL_C_neck_swallowShape', u'CTRL_L_jaw_chinCompress',
                     u'CTRL_R_jaw_ChinRaiseD', u'CTRL_L_jaw_ChinRaiseD', u'CTRL_L_jaw_clench',
                     u'CTRL_R_jaw_chinCompress',
                     u'CTRL_R_jaw_clench', u'CTRL_C_jaw', u'CTRL_C_jaw_fwdBack', u'CTRL_L_neck_stretch',
                     u'CTRL_L_neck_mastoidContract', u'CTRL_R_neck_stretch', u'CTRL_C_jaw_openExtreme',
                     u'CTRL_neck_throatUpDown', u'CTRL_neck_digastricUpDown', u'CTRL_neck_throatExhaleInhale',
                     u'CTRL_R_neck_mastoidContract', u'CTRL_rigLogicSwitch', u'CTRL_lookAtSwitchShape',
                     u'CTRL_R_mouth_lipBiteD', u'CTRL_L_mouth_lipBiteD', u'CTRL_R_mouth_lipsTowardsTeethU',
                     u'CTRL_L_mouth_lipsTowardsTeethU', u'CTRL_L_mouth_lipsTowardsTeethD',
                     u'CTRL_R_mouth_lipsTowardsTeethD', u'CTRL_R_mouth_towardsU', u'CTRL_L_mouth_towardsD',
                     u'CTRL_L_mouth_towardsU', u'CTRL_R_mouth_funnelU', u'CTRL_R_mouth_towardsD',
                     u'CTRL_L_mouth_funnelU',
                     u'CTRL_L_mouth_funnelD', u'CTRL_R_mouth_funnelD', u'CTRL_R_mouth_lipsTogetherD',
                     u'CTRL_L_mouth_lipsTogetherD', u'CTRL_L_mouth_lipsTogetherU', u'CTRL_R_mouth_lipsTogetherU',
                     u'CTRL_R_mouth_pressU', u'CTRL_L_mouth_pressU', u'CTRL_L_mouth_pressD', u'CTRL_R_mouth_pressD',
                     u'CTRL_C_teethU', u'CTRL_C_teethD', u'CTRL_C_mouth_lipShiftU', u'CTRL_C_teeth_fwdBackU',
                     u'CTRL_C_teeth_fwdBackD', u'CTRL_C_mouth_lipShiftD', u'CTRL_convergenceSwitch',
                     u'CTRL_R_brow_down',
                     u'CTRL_L_brow_raiseIn', u'CTRL_R_brow_raiseIn', u'CTRL_L_brow_raiseOut', u'CTRL_R_brow_raiseOut',
                     u'CTRL_L_brow_down', u'CTRL_C_eye', u'CTRL_L_brow_lateral', u'CTRL_R_brow_lateral', u'CTRL_R_eye',
                     u'CTRL_L_eye_squintInner', u'CTRL_L_eye', u'CTRL_R_eye_squintInner', u'CTRL_L_eye_cheekRaise',
                     u'CTRL_R_eye_blink', u'CTRL_R_eye_pupil', u'CTRL_L_eye_blink', u'CTRL_L_eye_pupil',
                     u'CTRL_R_eye_cheekRaise', u'CTRL_C_eye_parallelLook', u'CTRL_L_eye_lidPress',
                     u'CTRL_R_eye_lidPress',
                     u'CTRL_R_nose', u'CTRL_R_ear_up', u'CTRL_L_ear_up', u'CTRL_L_nose', u'CTRL_C_mouth',
                     u'CTRL_R_nose_wrinkleUpper', u'CTRL_L_nose_wrinkleUpper', u'CTRL_L_mouth_upperLipRaise',
                     u'CTRL_R_mouth_upperLipRaise', u'CTRL_R_mouth_cornerPull', u'CTRL_L_mouth_sharpCornerPull',
                     u'CTRL_R_mouth_sharpCornerPull', u'CTRL_L_mouth_cornerPull', u'CTRL_L_mouth_dimple',
                     u'CTRL_R_mouth_dimple', u'CTRL_L_mouth_cornerDepress', u'CTRL_R_mouth_cornerDepress',
                     u'CTRL_L_mouth_stretch', u'CTRL_R_mouth_stretch', u'CTRL_R_mouth_lowerLipDepress',
                     u'CTRL_L_mouth_lowerLipDepress', u'CTRL_L_mouth_suckBlow', u'CTRL_R_mouth_suckBlow',
                     u'CTRL_R_mouth_stretchLipsClose', u'CTRL_L_mouth_purseU', u'CTRL_R_mouth_purseU',
                     u'CTRL_L_mouth_stretchLipsClose', u'CTRL_L_mouth_purseD', u'CTRL_R_mouth_purseD',
                     u'CTRL_L_mouth_corner', u'CTRL_L_eye_eyelidU', u'CTRL_R_eye_eyelidU', u'CTRL_L_eye_eyelidD',
                     u'CTRL_R_mouth_corner', u'CTRL_R_eye_eyelidD', u'CTRL_neckCorrectivesMultiplyerU',
                     u'CTRL_neckCorrectivesMultiplyerM', u'CTRL_neckCorrectivesMultiplyerD']
        cmds.bakeResults(bake_face, simulation=True,
                         t=(int(cmds.playbackOptions(q=True, min=True)), int(cmds.playbackOptions(q=True, max=True))))
        anm_curves = cmds.listConnections(face_export, type="animCurve")
        cmds.select(face_export, r=True)
        cmds.select(anm_curves, add=True)
        cmds.file(face_export_name, force=True, options="v=0;", typ="FBX export", pr=True, es=True)
        cmds.delete(anm_curves, "rig")

    def create_export_config(self):
        export_config_path = self.get_export_path() + "config.json"
        sets = "sets"
        scene = {}
        shots_arr = {}
        chars_arr = {}
        scene_name = cmds.file(q=True, sceneName=True, shortName=True).split(".")[0]
        scene['name'] = scene_name
        shots = cmds.ls(type="shot")
        chars = self.get_chars()
        for shot in shots:
            camera = cmds.listConnections(shot, type="camera")
            start_frame = cmds.getAttr("{}.startFrame".format(shot))
            end_frame = cmds.getAttr("{}.endFrame".format(shot))
            single_shot = {"camera": camera, 'start': start_frame, "end": end_frame}
            shots_arr[shot] = single_shot
        for i in range(len(chars)):
            if cmds.objExists(sets):
                offset_x = cmds.getAttr("{}:rig:World.translateX".format(chars[i])) + (
                        cmds.getAttr("{}.translateX".format(sets)) * -1)
                offset_y = cmds.getAttr("{}:rig:World.translateY".format(chars[i])) + (
                        cmds.getAttr("{}.translateY".format(sets)) * -1)
                offset_z = cmds.getAttr("{}:rig:World.translateZ".format(chars[i])) + (
                        cmds.getAttr("{}.translateZ".format(sets)) * -1)
            else:
                offset_x = cmds.getAttr("{}:rig:World.translateX".format(chars[i]))
                offset_y = cmds.getAttr("{}:rig:World.translateY".format(chars[i]))
                offset_z = cmds.getAttr("{}:rig:World.translateZ".format(chars[i]))
            single_char = {"name": chars[i], 'offset_x': offset_x, "offset_y": offset_y, "offset_z": offset_z}
            chars_arr[chars[i]] = single_char
        scene['shots'] = shots_arr
        scene['chars'] = chars_arr

        with open(export_config_path, 'w') as file:
            json_string = json.dumps(scene, default=lambda o: o.__dict__, sort_keys=True, indent=2)
            file.write(json_string)

    def publish(self):
        if not self.check_scene():
            print("SCENE DOES NOT CORRECTED")
            return False
        self.export_cameras()
        self.check_scene()
        chars = self.list_all_children("chars_grp")
        for i in range(len(chars)):
            self.export_body(chars[i])
            self.export_face(chars[i])
        self.create_export_config()
        print("SCENE FINAL COMPLETE")
        return True

    def export_anm_from_scene(self, parametrs):

        def get_all_children_with_anim(selected_objects):
            all_objects = []
            for obj in selected_objects:
                all_objects.append(obj)
                obj_elements = cmds.listRelatives(obj, allDescendents=True, f=True)
                for element in obj_elements:
                    all_objects.append(element)
                    anim_nodes = cmds.listConnections(element, type='animCurve')
                    if anim_nodes:
                        all_objects.extend(anim_nodes)
            return all_objects

        source_scene_path = parametrs[0]
        target_scene_path = parametrs[1]
        char_valid_names = parametrs[2]["name"]
        start_time = parametrs[3]
        end_time = parametrs[4]

        cmds.file(source_scene_path, o=True, f=True)
        source_active_char = None

        if cmds.objExists('chars_grp'):
            source_chars = cmds.listRelatives('chars_grp', c=True)
            for char in source_chars:
                for valid in char_valid_names:
                    if valid in char:
                        source_active_char = char
            else:
                # do reference node query
                pass
        '''reload'''
        root_node = cmds.ls(source_active_char, rn=True)
        r_node = cmds.referenceQuery(root_node, rfn=True)
        ref = cmds.referenceQuery(r_node, f=True)
        this_char_file = cmds.referenceQuery(r_node, filename=True, shortName=True)
        ref_new = str(ref.replace(this_char_file, parametrs[2]["file"]))
        tr_out = cmds.file(ref_new, loadReference=r_node)
        '''vsrs'''
        source_active_char_root = ":" + source_active_char.split(":")[-1]
        namespace = source_active_char.replace(source_active_char_root, "")
        general_ct = namespace + ":" + parametrs[2]["ct"]
        bake_set = cmds.sets(namespace + ":" + "OUT", q=True)
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
        bake_set = bake_set + loc_zero
        cmds.bakeResults(bake_set, t=(start_time, end_time))
        cmds.delete(loc_zero[0] + "_parentConstraint1")
        cmds.parentConstraint(loc_zero, general_ct, weight=1)
        cmds.cutKey(get_cam)
        cam_attrs = [".translateX", ".translateY", ".translateZ", ".rotateX", ".rotateY", ".rotateZ", ]
        for attr in cam_attrs:
            if cmds.getAttr(get_cam[0] + str(attr), l=True):
                try:
                    cmds.setAttr(get_cam[0] + str(attr), l=False)
                    cmds.setAttr(get_cam[0] + str(attr), 0)
                except:
                    pass

        transfer_exp = cmds.duplicate(bake_objs, name=transfer_exp_name)

        bake_objs_all = cmds.listRelatives(bake_objs, allDescendents=True, f=True)
        transfer_exp_all = cmds.listRelatives(transfer_exp, allDescendents=True, f=True)

        for i in range(len(bake_objs_all)):
            try:
                cmds.copyKey(bake_objs_all[i], time=(
                cmds.playbackOptions(q=True, minTime=True), cmds.playbackOptions(q=True, maxTime=True)))
                cmds.pasteKey(transfer_exp_all[i])
            except:
                pass

        cmds.parent(transfer_exp[0], w=True)
        cmds.select(get_all_children_with_anim(cmds.ls(transfer_exp[0])))
        target_scene_dir = target_scene_path.replace(target_scene_path.split("/")[-1], "")
        if not os.path.exists(target_scene_dir):
            os.makedirs(target_scene_dir)
        cmds.file(target_scene_path, force=True, options="v=0;", typ="mayaAscii", es=True)
