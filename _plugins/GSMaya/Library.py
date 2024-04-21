import json
import sys
import maya.cmds as cmds
import os
import time
import subprocess


class Library:
    def __init__(self):
        self.config = None
        self.project_path = None
        self.resolution = (1920, 1080)
        self.playblast_path = None
        self.scene_path = None
        self.ffmpeg_path = "ffmpeg path"
        self.seria_start = 0
        self.sharp = None
        self.pattern = None
        self.cldr = None
        self.cldr2 = None

    def set_config(self):
        with open(r'D:\test.json', 'w') as f:
            self.config = json.load(f)
            self.pattern = self.config["pattern"]
            self.cldr = self.config["cldr"]
            self.cldr2 = self.config["cldr2"]
    def get_project_path(self):
        return self.project_path

    def set_project(self, project_path):
        self.project_path = project_path
        if os.path.isdir(project_path + "/Scenes"):
            self.scene_path = project_path + "/Scenes"
        elif os.path.isdir(project_path + "/Scene"):
            project_path + "/Scene"
        if os.path.isdir(project_path + "/Playblast"):
            self.playblast_path = project_path + "/Playblast"
        elif os.path.isdir(project_path + "/Playblasts"):
            self.playblast_path = project_path + "/Playblasts"

    def set_resolution(self, resolution):
        if len(resolution) != 2:
            return False
        if not isinstance(resolution, tuple):
            return False
        self.resolution = resolution

    def get_resolution(self):
        return self.resolution

    def quick_playblast(self, output_dir_path, filename, frame_range=(1, 120), resolution=(1920, 1080),
                        encoding=("mov", "h264"), camera="persp", overwrite=True, shots=False):
        path = "/GSMaya"
        if not path in sys.path:
            sys.path.append(path)
            print("pathed")
        from zurbrigg_playblast import ZurbriggPlayblast

        playblast = ZurbriggPlayblast()
        playblast.set_ffmpeg_path(self.ffmpeg_path)
        padding = 4
        overscan = False
        show_ornaments = True
        show_in_viewer = False
        playblast.set_frame_range(frame_range)
        cmds.setFocus("modelPanel1")
        playblast.set_resolution(resolution)
        playblast.set_encoding(encoding[0], encoding[1])
        playblast.set_camera(camera)
        playblast.execute(output_dir_path, filename, padding, overscan, show_ornaments, show_in_viewer, overwrite,
                          shots)

    def get_non_blasded_scene(self):

        scenes = []
        for scene in os.listdir(self.scene_path):
            if self.pattern in scene:
                if scene[0] == "#" and not self.sharp:
                    continue
                elif scene[0] == "#" and self.sharp:
                    scenes.append(scene)
                else:
                    scenes.append(scene)


        non_blasted = []
        blasts = []
        if os.listdir(self.playblast_path):
            for blast in os.listdir(self.playblast_path):
                blasts.append(blast.split(".")[0])
        else:
            for scene in scenes:
                clear_name = scene.split(self.pattern)[0]
                non_blasted.append(scene)
            return non_blasted
        for scene in scenes:
            clear_name = scene.split(self.pattern)[0]
            if not clear_name in blasts:
                non_blasted.append(scene)

        return non_blasted

    def get_trash_blastes(self):

        blasts = []
        for blast in os.listdir(self.playblast_path):
            blasts.append(blast)

        scenes = []
        for scene in os.listdir(self.scene_path):
            if self.pattern in scene:
                scenes.append(scene.split(self.pattern)[0])

        trash_blast = []
        for blast in blasts:
            if not blast.split(".")[0] in scenes:
                trash_blast.append(blast)
        return trash_blast

    def delete_trash_blasts(self):

        trash_blastes = self.get_trash_blastes()
        non_deleted = []
        for blast in trash_blastes:
            try:
                os.remove(self.playblast_path + "/" + blast)
                print(self.playblast_path + "/" + blast)
            except:
                non_deleted.append(blast)
        if non_deleted:
            return non_deleted
        else:
            return True

    def playblast_queue(self, sharp=False):
        self.delete_trash_blasts()
        non_blasted_scenes = self.get_non_blasded_scene()

        all_scenes = len(non_blasted_scenes)

        for scene in range(len(non_blasted_scenes)):

            if non_blasted_scenes[scene][0] == "#" and not sharp:
                continue

            if scene != 0:
                before_scene_full_path = self.scene_path + "/" + non_blasted_scenes[scene-1]
                before_scene_name = non_blasted_scenes[scene-1].split(self.pattern)[0]
                before_playblast_file = self.playblast_path + "/" + before_scene_name + ".mov"
                if not os.path.exists(before_playblast_file):
                    os.rename(before_scene_full_path, before_scene_full_path.replace(before_scene_name, "#" + before_scene_name))
                elif os.path.getsize(before_playblast_file) == 0:
                    os.remove(before_playblast_file)
                    os.rename(before_scene_full_path, before_scene_full_path.replace(scene_name, "#" + scene_name))

            scene_full_path = self.scene_path + "/" + non_blasted_scenes[scene]
            time.sleep(1)
            try:
                cmds.file(scene_full_path, o=True, f=True, ignoreVersion=True, prompt=False)
            except:
                continue
            scene_name = non_blasted_scenes[scene].split(self.pattern)[0]
            startFrame = cmds.playbackOptions(q=True, animationStartTime=True)
            endFrame = cmds.playbackOptions(q=True, animationEndTime=True)
            time.sleep(1)
            try:
                self.quick_playblast(self.playblast_path, scene_name, frame_range=(startFrame, endFrame),
                                     resolution=self.resolution,
                                     encoding=("mov", "h264"),
                                     camera=self.get_camera(), overwrite=True, shots=False)
            except:
                pass

    def get_camera(self):
        camera = cmds.file(q=True, sn=True, shn=True).split(self.pattern)[0]
        if cmds.objExists(camera):
            if cmds.objectType(cmds.listRelatives(camera, shapes=True)[0]):
                return camera

        if cmds.objExists("cameras_grp"):
            camera = cmds.listRelatives("cameras_grp")[0]
            return camera
        else:
            get_cam = cmds.ls(type="camera")
            for elem in get_cam:
                for i in self.cldr:
                    if self.cldr[i] in elem and self.cldr2[i] in elem:
                        return cmds.listRelatives(elem, parent=True)[0]


        return "persp"


