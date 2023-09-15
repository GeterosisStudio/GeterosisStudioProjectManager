import sys
GETEROSIS_PROJECT_MANAGER_PATH = 'E:/Projects/core/GeterozisProjectManager/GeterosisProjectManager/'
if not GETEROSIS_PROJECT_MANAGER_PATH in sys.path:
    sys.path.insert(1, GETEROSIS_PROJECT_MANAGER_PATH)
GSPM_MAYA_SCENE_CLS = None
import GSMaya.ProjectManager.main
reload(GSMaya.ProjectManager.main.main())
GSMaya.ProjectManager.main.main()