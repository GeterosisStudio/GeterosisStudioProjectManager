import maya.cmds as cmds

keys = cmds.keyframe("sr070ep08sc10_translateZ", query=True)
for key in keys:
    print(key)
    value = cmds.keyframe("sr070ep08sc10_translateZ", time=(key, key), query=True, valueChange=True)
    print("value ={}".format(value[0]))
    tangent = cmds.keyTangent("sr070ep08sc10_translateZ", q=1, time=(key, key), inAngle=1, inWeight=1, itt=1, ott=1,
                              outAngle=1, outWeight=1)
    print(tangent)






