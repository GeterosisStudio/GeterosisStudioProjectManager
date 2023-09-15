""" This module backup project, main function -  project_backup"""
import os
import shutil
import Log
import json


exeptions = {}
def delete_old(source_dir, target_dir, root_target_dir, old_dir):
    dir_list = os.listdir(target_dir)
    for dir_obj in dir_list:
        if dir_obj == "_old":
            continue
        target_obj = target_dir + "/" + dir_obj
        source_path = source_dir + "/" + dir_obj
        old_path = target_obj.replace(root_target_dir, old_dir)
        if not os.path.exists(source_path):
            if os.path.isdir(target_obj):
                Log.info("_OLD COPY to: {}".format(target_obj))
                shutil.copytree(target_obj, old_path)
                Log.info("_OLD DELETE to: {}".format(target_obj))
                shutil.rmtree(target_obj)
            if os.path.isfile(target_obj):
                Log.info("_OLD COPY to: {}".format(old_path))
                if os.path.isfile(old_path):
                    os.remove(old_path)
                if not os.path.exists(old_path.replace("/" + dir_obj, "")):
                    os.makedirs(old_path.replace("/" + dir_obj, ""))
                shutil.copy(target_obj, old_path)
                Log.info("_OLD DELETE to: {}".format(target_obj))
                os.remove(target_obj)

        elif os.path.isdir(target_obj):
            Log.info("INTO (DELETE OLD): {}".format(target_obj))
            try:
                delete_old(source_path, target_obj, root_target_dir, old_dir)
            except:
                Log.warning("DELETE OLD FAILED: {0} to {1}".format(source_dir, target_obj))
                exeptions[source_dir] = (target_obj)


def copy_dirs(source_dir, target_dir):
    if not os.path.isdir(target_dir):
        shutil.copytree(source_dir, target_dir)
        return True
    else:
        dir_list = os.listdir(source_dir)
        for dir_obj in dir_list:
            source_obj = source_dir + "/" + dir_obj
            source_time = os.path.getmtime(source_obj)
            target_obj = source_obj.replace(source_dir, target_dir)

            if os.path.isdir(source_obj) and not os.path.exists(target_obj):
                Log.info("Coping: {0} to {1}".format(source_obj, target_obj))
                shutil.copytree(source_obj, target_obj)
                Log.info("Copied: {0} to {1}".format(source_obj, target_obj))

            elif os.path.isdir(source_obj) and os.path.exists(target_obj):
                Log.info("Do sync: {0}".format(source_obj))
                try:
                    copy_dirs(source_obj, target_obj)
                except:
                    Log.warning("BACKUP FAILED: {0} to {1}".format(source_obj, target_obj))
                    exeptions[source_obj] = (target_obj)



        else:
                if os.path.isfile(source_obj) and not os.path.exists(target_obj):
                    Log.info("Coping: {0} to {1}".format(source_obj, target_obj))
                    shutil.copy(source_obj, target_obj)
                    Log.info("Copied: {0} to {1}".format(source_obj, target_obj))

                elif os.path.exists(target_obj):
                    target_time = os.path.getmtime(target_obj)
                    if source_time > target_time:
                        try:
                            Log.info("Coping: {0} to {1}".format(source_obj, target_obj))
                            os.remove(target_obj)
                            shutil.copy(source_obj, target_obj)
                            Log.info("Copied: {0} to {1}".format(source_obj, target_obj))
                        except:
                            Log.warning("BACKUP FAILED: {0} to {1}".format(source_obj, target_obj))
                            exeptions[source_obj] = (target_obj)

def project_backup(source_dir, target_dir):
    copy_dirs(source_dir, target_dir)
    root_target_dir = target_dir
    old_dir = target_dir + "/" + "_old"
    delete_old(source_dir, target_dir, root_target_dir, old_dir)
    Log.info("BACKUP COMPLETE: {} TO {}.".format(source_dir, target_dir))
    if exeptions != {}:
        if not os.path.exists(source_dir + "/Logs/"):
            os.mkdir(source_dir + "/Logs/")
        with open(source_dir + "/Logs/Bacup.json", 'w') as f:
            json.dump(exeptions, f)
        Log.info("BACKUP FAILEDS: {}".format(exeptions))


project_backup("E:/Projects", "Y:/MUSOR/Projects")
