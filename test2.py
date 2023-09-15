import sys
plugin_path = 'E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/'
if not plugin_path in sys.path:
    sys.path.insert(1, plugin_path)
import GSMaya.MayaStartupScript as MayaStartupScript
reload(MayaStartupScript)
MayaStartupScript.maya_startup()
