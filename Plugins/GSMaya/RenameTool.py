import maya.cmds as cmds
import string


class RenameTool:
    def __init__(self, windowID):
        if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID, windowID + 'dock')

        self.win = cmds.window(windowID, title='Rename Tool', resizeToFitChildren=True, sizeable=False, mxb=False,
                               mnb=False)
        self.tabs = cmds.tabLayout()

        # First Tab #
        global NameField, PrefixField, SuffixField

        firstTab = cmds.rowColumnLayout(rs=[1, 5], cs=[1, 5])
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[firstTab, 'Rename'])
        cmds.separator(h=1, style='none')

        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 130), (2, 50)], columnOffset=[(1, 'both', 2)],
                             cs=[2, 5])
        NameField = cmds.textField(pht='Name', ann='Name')
        cmds.button(label='Rename', command=self.Rename)
        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 90), (2, 90)], columnOffset=[(1, 'both', 2)],
                             cs=[2, 7])
        PrefixField = cmds.textField(pht='Prefix', ann='Prefix')
        SuffixField = cmds.textField(pht='Suffix', ann='Suffix')
        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 90), (2, 90)], columnOffset=[(1, 'both', 2)],
                             cs=[2, 7])
        cmds.button(label='Add Affixes', command=self.AddAffix)
        cmds.button(label='Remove Affixes', command=self.RemoveAffix)
        cmds.setParent('..')
        cmds.setParent('..')

        # Second Tab #
        global ReplaceNameField, WithNameField

        secondTab = cmds.rowColumnLayout(rs=[1, 7], cs=[1, 5])
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[secondTab, 'Replace'])
        cmds.separator(h=1, style='none')

        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 180)], columnOffset=[(1, 'both', 2)], cs=[1, 1])
        ReplaceNameField = cmds.textField(pht="Search for...")
        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 180)], columnOffset=[(1, 'both', 2)], cs=[1, 1])
        WithNameField = cmds.textField(pht="Replace with...")
        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 50), (2, 100), (3, 50)], columnOffset=[(1, 'both', 3)],
                             cs=[1, 1])
        cmds.separator(h=1, style='none')
        cmds.button(label='Replace', command=self.Replace)
        cmds.setParent('..')

        allowedAreas = ['right', 'left']
        self.dock = cmds.dockControl(windowID + 'dock', l='Rename Tool', area='left', content=windowID,
                                     allowedArea=allowedAreas, fl=True)
        cmds.window(windowID + 'dock', edit=True, widthHeight=(200, 125))


    def Rename(self, *args):
        global NameField

        objName = cmds.textField(NameField, query=True, text=True)

        objList = cmds.ls(sl=True, selection=True)
        for obj in objList:
            if (objList.index(obj) < 9):
                cmds.rename(obj, objName + '0' + str(objList.index(obj) + 1))
            else:
                cmds.rename(obj, objName + str(objList.index(obj) + 1))

    def AddAffix(self, *args):
        global PrefixField, SuffixField

        objPrefix = cmds.textField(PrefixField, query=True, text=True)
        objSuffix = cmds.textField(SuffixField, query=True, text=True)

        objList = cmds.ls(sl=True, selection=True)
        for obj in objList:
            if (objPrefix != ""):
                obj = cmds.rename(obj, objPrefix + "_" + obj)
            if (objSuffix != ""):
                cmds.rename(obj, obj + "_" + objSuffix)

    def RemoveAffix(self, *args):
        global PrefixField, SuffixField

        objPrefix = cmds.textField(PrefixField, query=True, text=True)
        objSuffix = cmds.textField(SuffixField, query=True, text=True)

        objList = cmds.ls(sl=True, selection=True)
        for obj in objList:
            if objPrefix != "" and obj.startswith(objPrefix) == True:
                obj = cmds.rename(obj, obj[len(objPrefix) + 1:])
            if objSuffix != "" and obj.endswith(objSuffix) == True:
                cmds.rename(obj, obj[:-len(objSuffix) - 1])

    def Replace(self, *args):
        global ReplaceNameField, WithNameField

        objToReplace = cmds.textField(ReplaceNameField, query=True, text=True)
        ReplaceWith = cmds.textField(WithNameField, query=True, text=True)
        ReplaceList = cmds.ls('*' + objToReplace + '*', type='transform')

        for obj in ReplaceList:
            if (ReplaceList.index(obj) < 9):
                cmds.rename(obj, string.replace(obj, objToReplace, ReplaceWith))
            else:
                cmds.rename(obj, string.replace(obj, objToReplace, ReplaceWith))


RenameTool('RenameToolWindow')