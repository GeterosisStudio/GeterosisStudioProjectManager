import maya.cmds as cmds

import pprint

ClearRoomList = []

BuildData = []

ApartamentData = []

RoomData = []

AssetData = []

cmds.select('Build', r=True, hi=True)

DirtRoomList = cmds.ls(selection=True, transforms=True)


def write_file(path, data):
    pathfile = open(path, 'w')
    pathfile.write(data)
    pathfile.close()


# create Clear Build
for i in range(len(DirtRoomList)):
    DirtRoomListElem = str(DirtRoomList[i])
    while True:
        if DirtRoomListElem[-1].isdigit():
            DirtRoomListElem = DirtRoomListElem.replace(DirtRoomListElem[-1], "")
        else:
            ClearRoomList.append(DirtRoomListElem)
            break

DirtRoomList.reverse()
ClearRoomList.reverse()

for i in range(len(ClearRoomList)):

    AssetName = ClearRoomList[i]
    Name = DirtRoomList[i]

    if AssetName != 'Room' and AssetName != 'Apartament' and AssetName != 'Build':
        tx = cmds.getAttr(Name + ".translateX")
        ty = cmds.getAttr(Name + ".translateY")
        tz = cmds.getAttr(Name + ".translateZ")

        rx = cmds.getAttr(Name + ".rotateX")
        ry = cmds.getAttr(Name + ".rotateY")
        rz = cmds.getAttr(Name + ".rotateZ")

        sx = cmds.getAttr(Name + ".scaleX")
        sy = cmds.getAttr(Name + ".scaleY")
        sz = cmds.getAttr(Name + ".scaleZ")

        AssetData = [AssetName, tx, ty, tz, rx, ry, rz, sx, sy, sz]
        RoomData.append(AssetData)

    if AssetName == 'Room':
        RoomData.reverse()
        ApartamentData.append(RoomData)
        RoomData = []

    if AssetName == 'Apartament':
        ApartamentData.reverse()
        BuildData.append(ApartamentData)
        ApartamentData = []

    if AssetName == 'Build':
        BuildData.reverse()

for i in range(len(BuildData)):
    for z in range(len(BuildData[i])):
        for x in range(len(BuildData[i][z])):
            print(BuildData[i][z][x])







