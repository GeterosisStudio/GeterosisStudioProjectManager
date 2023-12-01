import sys
GETEROSIS_PROJECT_MANAGER_PATH = '//'
if not GETEROSIS_PROJECT_MANAGER_PATH in sys.path:
    sys.path.insert(1, GETEROSIS_PROJECT_MANAGER_PATH)
GSPM_MAYA_SCENE_CLS = None
reload(Plugins.GSMaya.ProjectManager.main.main())
Plugins.GSMaya.ProjectManager.main.main()