import shutil
import os


def rename_files(files_dir, old_prefix, new_prefix):
    filenames = next(os.walk(files_dir), (None, None, []))[2]
    for i in range(len(filenames)):
        if old_prefix in filenames[i]:
            renamed = filenames[i].replace(old_prefix, new_prefix)
            rf = files_dir + filenames[i]
            rn = files_dir + renamed
            os.rename(rf, rn)


def check_file_exist(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


def create_dir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def get_default_project_dir():
    return __file__.replace("GSMain/File.py", "DefaultProject/")


def copy_file(source_file, new_file):
    shutil.copyfile(source_file, new_file)


def get_default_project_file(file_type, ext=False):
    default_proj_file_dir = get_default_project_dir() + "Default_Files/"
    file_types = {"maya": default_proj_file_dir + "Untitled.ma",
                  "premiere": default_proj_file_dir + "Untitled.prproj",
                  "scenary": default_proj_file_dir + "Untitled.rtf",
                  }
    if ext:
        file_ext = {"maya": ".ma",
                    "premiere": ".prproj",
                    "scenary": ".rtf",
                    }
        return file_ext[file_type]
    return file_types[file_type]


def get_project_dir():
    return None


def get_local_dir(dir_name):
    returned_dir = get_project_dir() + dir_name
    return returned_dir


def create_anim_scene(scene_name):
    """
    :param scene_name: e0010s0000d0000v0000
    """
    episode_name = scene_name[:5]
    full_dir_scene = "animation/Scenes/" + episode_name + "/" + scene_name + "/"
    full_dir_path = get_local_dir(full_dir_scene)
    work_dir = full_dir_path + "work/"
    audio_dir = full_dir_path + "audio/"
    export_audio_dir = full_dir_path + "export/audio/"
    export_cameras_dir = full_dir_path + "export/cameras/"
    create_dir(work_dir)
    create_dir(audio_dir)
    create_dir(export_audio_dir)
    create_dir(export_cameras_dir)

    if not check_file_exist(work_dir + scene_name + '.0001' + get_default_project_file("maya", ext=True)):
        copy_file(get_default_project_file("maya"),
                  work_dir + scene_name + '.0001' + get_default_project_file("maya", ext=True))
        print("CREATED:", scene_name + get_default_project_file("maya", ext=True))
    else:
        print("EXIST:", scene_name + get_default_project_file("maya", ext=True))

    if not check_file_exist(full_dir_path + scene_name + get_default_project_file("scenary", ext=True)):
        copy_file(get_default_project_file("scenary"),
                  full_dir_path + scene_name + get_default_project_file("scenary", ext=True))
        print("CREATED:", scene_name + get_default_project_file("scenary", ext=True))
    else:
        print("EXIST:", scene_name + get_default_project_file("scenary", ext=True))

    if not check_file_exist(full_dir_path + scene_name + get_default_project_file("premiere", ext=True)):
        copy_file(get_default_project_file("premiere"),
                  full_dir_path + scene_name + get_default_project_file("premiere", ext=True))
        print("CREATED:", scene_name + get_default_project_file("scenary", ext=True))
    else:
        print("EXIST:", scene_name + get_default_project_file("premiere", ext=True))
    return full_dir_path


def open_file(file_path):
    return os.startfile(file_path)


def read_file(file_pathes):
    file = open(file_pathes, 'r')
    string_list = []
    for line in file:
        string_list.append(line.rstrip())
    return string_list


def create_number_index(value, v=False):
    value = int(value)
    if not v:
        if value < 10:
            strig_lin = "00" + str(value) + "0"
            return strig_lin
        if 10 <= value < 100:
            strig_lin = "0" + str(value) + "0"
            return strig_lin
        if 100 <= value < 1000:
            strig_lin = str(value) + "0"
            return strig_lin
        if 1000 <= value:
            strig_lin = str(value)
            return strig_lin
    else:
        if value < 10:
            strig_lin = "00" + str(value) + "0"
            return strig_lin
        if 10 <= value < 100:
            strig_lin = "00" + str(value)
            return strig_lin
        if 100 <= value < 1000:
            strig_lin = str(value) + "0"
            return strig_lin
        if 1000 <= value:
            strig_lin = str(value)
            return strig_lin


def short_name_anm_scene_return(short_anm_name):
    break_value = short_anm_name.split(".")
    episode_index = create_number_index(break_value[0])
    scene_index = create_number_index(break_value[1])
    dialogue_index = create_number_index(break_value[2])
    version_index = create_number_index(break_value[3], v=True)
    scene_full_name = "e" + episode_index + "s" + scene_index + "d" + dialogue_index + "v" + version_index
    return scene_full_name


def create_scenes_with_mind_file(file_path):
    imported_list = read_file(file_path)
    corrected_scene_list = []
    for i in range(len(imported_list)):
        if imported_list[i] == '':
            continue
        if " " in imported_list[i]:
            imported_list[i] = "".join(imported_list[i].split())
        corrected_elem = short_name_anm_scene_return(imported_list[i])

        corrected_scene_list.append(corrected_elem)
    for i in range(len(corrected_scene_list)):
        create_anim_scene(corrected_scene_list[i])


def check_is_scene(file_path):
    "TODO reafct with regular"
    pattern_scene = get_project_dir() + 'animation/scenes/e'
    scene_name = file_path.split("/")[-1]

    if pattern_scene in file_path and len(scene_name) == 20:
        return True
    else:
        return False

