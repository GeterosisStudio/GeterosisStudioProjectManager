import maya.cmds as cmds

class Sequencer(Cameras_List, Shot_Time_List):
    @staticmethod
    
    def Create_Shot(name, start, end, cam):
        cmds.shot(name, st=start, et=end, cc=cam, sst=start, set=end)

    def set_cameras():
        if cmds.objExists("cameras_grp"):
            return("cameras_grp")
        if cmds.objExists("Cameras_grp"):
            cmds.rename("Cameras_grp", "cameras_grp")
            return("cameras_grp")
        else:
            cmds.group(em = True, name = "cameras_grp")
            return("cameras_grp")
    cam_grp = set_cameras()  
    print(cam_grp)


#импорт камер
cmds.file ("C:/Users/Admiral/Desktop/bufer/sas.ma", i = True)
cmds.parent("ep03sc01", "cameras")
pre_select = cmds.ls(selection = True)
cmds.select('cameras', hierarchy = True)
cmds.select("cameras", d = True)
cams = cmds.ls(selection = True, cameras = True)




cmds.select = (pre_select)


camera_list = ["persp1", "persp2", "persp3"]
start_list = [1, 30, 45]
end_list = [29, 44, 50]

if len(camera_list) == len(start_list) == len(end_list):
    shot_call = len(camera_list)

    for i in range(shot_call):
        name = "shot"
        start = start_list[i]
        end = end_list[i]
        cam = camera_list[i]
        Sequencer.Create_Shot(name, start, end, cam)
