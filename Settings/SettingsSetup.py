import json

libs = {"lib1": "Y:/MUSOR/Libraries/Animation/", "lib2": "Y:/MUSOR/LIBRARIES2/Animations/", "lib3": "D:/LIBRARIES3/Animations/"}

l_rooter = {"libs": libs}

lib_projects = {"ln": "Melnitsa/Luntik/scenes/", "lnt": "Melnitsa/Luntik/scenes/", "ln3": "Melnitsa/Luntik3d/scenes/",
            "lnt3": "Melnitsa/Luntik3d/scenes/",
            "sb": "Melnitsa/Sobaki/scenes/", "sbk": "Melnitsa/Sobaki/Scenes/", "sb3": "Melnitsa/Sobaki3d/Scenes/",
            "sbk3": "Melnitsa/Sobaki3d/Scenes/",
            "ts": "Melnitsa/Tsarevny/Scenes/", "urf1": "Melnitsa/Urfin1/Scenes/", "urf2": "Melnitsa/Urfin2/Scenes/",
            "sh": "Melnitsa/Shelkun/Scenes/",
            "shk": "Melnitsa/Shelkun/Scenes/", "ml": "Melnitsa/Malish/Scenes/", "mlh": "Melnitsa/Malish/Scenes/",
            "ml2": "Melnitsa/Malysh2/Scenes/",
            "mlh2": "Melnitsa/Malysh2/Scenes/", "qq": "qq/scenes/"}

l_rooter["projects"] = lib_projects

chars = {}
chars["ln"] = {"name": ["lk", "ln" "luntik"], "file": ["ln_OUT.mb", "luntik_OUT.mb"], "ct": "general_CT"}
chars["lk"] = {"name": ["lk", "ln" "luntik"], "file": ["ln_OUT.mb", "luntik_OUT.mb"], "ct": "general_CT"}
chars["ly"] = {"name": ["lunya", "ly"], "file": ["ln_OUT.mb", "lunya_OUT.mb"], "ct": "general_CT"}
chars["kz"] = {"name": ["kz", "kuzya"], "file": ["kz_OUT.mb", "kuzya_OUT.mb"], "ct": "general_CT"}
chars["bt"] = {"name": ["botanik"], "file": ["botanik_middle_OUT.mb"], "ct": "general_CT"}
chars["MH"] = {"name": ["MetaHumanB_F"], "file": ["MetaHumanB_F_OUT.ma"], "ct": "rig:General"}
chars["vr"] = {"name": ["vr", "var", "varya"], "file": ["varvara_OUT.ma"], "ct": "rig:General"}
chars["sn"] = {"name": ["sn", "son", "sona", "sonya"], "file": ["sonya_OUT.ma"], "ct": "rig:General"}
chars["vr"] = {"name": ["vr", "var", "varya"], "file": ["varvara_OUT.ma"], "ct": "rig:General"}
chars["vs"] = {"name": ["vs", "vas", "vasilisa"], "file": ["vasilisa_OUT.ma"], "ct": "rig:General"}
chars["mr"] = {"name": ["mr", "mar", "marlen"], "file": ["marlen_OUT.ma"], "ct": "rig:General"}
chars["ks"] = {"name": ["ks", "kosh", "koshey"], "file": ["koshey_OUT.ma"], "ct": "rig:General"}
chars["kt"] = {"name": ["kt", "kot"], "file": ["kot_OUT.ma"], "ct": "rig:General"}
chars["ds"] = {"name": ["dasha"], "file": "dasha_middle_OUT.mb", "ct": "general_CT"}


l_rooter["chars"] = chars

projects = {"illusion": {"name": "ILLUSION", "prod_path": "E:/Projects/ILLUSION_1/"}}


config = {}

config["programs"] = {
  "WinRAR": "E:/ProgramFiles/WinRAR/WinRAR.exe",
  "ffmpeg": "E:/Projects/core/ffmpeg/ffmpeg4/bin/ffmpeg.exe",
  "maya": "C:/Program Files/Autodesk/Maya2020/bin/maya.exe",
}

config["settings"] = {"custom settings": False, "custom settings path": None}

with open('C:/Users/AlexLip/Documents/GeterosisProjectManager/Settings/Libraries.json', 'w') as f:
    json.dump(l_rooter, f, indent=4)

with open('C:/Users/AlexLip/Documents/GeterosisProjectManager/Settings/Projects.json', 'w') as f:
    json.dump(projects, f, indent=4)

with open('C:/Users/AlexLip/Documents/GeterosisProjectManager/Settings/Config.json', 'w') as f:
    json.dump(config, f, indent=4)