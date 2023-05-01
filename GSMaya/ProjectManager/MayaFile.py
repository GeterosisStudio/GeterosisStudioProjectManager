import maya.cmds as cmds
import os


class MayaFile:

    def __init__(self):
        self.project_name = None
        self.project_path = None

    def work_incremental_save(self, path=None):
        if not path:
            path = cmds.file(q=True, sceneName=True)
        if not "work/" in path:
            short_name = cmds.file(q=True, sceneName=True, shortName=True)
            work_path = path.replace(short_name, "") + "work/"
            work_scene_path = work_path + short_name
            path = work_scene_path

        scene_path = path
        path, file = os.path.split(scene_path)
        file = file.split('.')
        file_name = file[0].split('_0')
        version = 1
        if len(file_name) > 1:
            version = int(file_name[-1]) + 1
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        while os.path.exists(name):
            version += 1
            name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        cmds.file(rename=name)
        cmds.file(save=True)
        return name

    def final_save(self):
        self.work_incremental_save()
        scene_path = cmds.file(q=True, sceneName=True)
        path, file = os.path.split(scene_path)
        file = file.split('.')
        file_name = file[0].split('_0')
        version = 1
        if len(file_name) > 1:
            version = int(file_name[-1]) + 1
        name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        while os.path.exists(name):
            version += 1
            name = os.path.join(path, '{}.{}.{}'.format(file_name[0], str(version).rjust(4, '0'), file[-1]))
        name = os.path.join(path, '{}.{}'.format(file_name[0], file[-1])).replace("/work", "")
        cmds.file(rename=name)
        cmds.file(save=True)

    def get_file_dir(self):
        return cmds.file(q=True, sceneName=True).replace("/work", "")
