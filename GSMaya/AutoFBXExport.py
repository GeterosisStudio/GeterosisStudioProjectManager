import maya.cmds as cmds

class AutoFBXExport_Window(object):

    # constructor
    def __init__(self):

        self.window = "MR_Window"
        self.title = "AutoFBXExport"
        self.size = (400, 70)

        # close old window is open
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        # create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)

        cmds.columnLayout(adjustableColumn=True)

        self.FilePath = cmds.textFieldGrp(label='File Path')

        self.FBXExport = cmds.button(label='Apply', command=self.AutoFBXExport)

        # display new window
        cmds.showWindow()




    def AutoFBXExport(self, *args):

        BuildList = cmds.ls(selection=True, transforms=True)

        for i in range(len(BuildList)):
            Path = cmds.textFieldGrp(self.FilePath, query=True, text=True) + "/" + BuildList[i] + ".fbx"
            print(Path)
            Elem = str(BuildList[i])
            print(Elem)
            cmds.select(BuildList[i], r=True)
            cmds.file(Path, es=True, force=True, options="v=0;", typ="FBX export", pr=True)


run = AutoFBXExport_Window()













