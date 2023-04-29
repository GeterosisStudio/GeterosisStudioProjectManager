import os
import pyttsx3
import os

project_path = None


def text_to_sound_pyttsx3(text, file, speed=1):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170 * speed)
    engine.save_to_file(text, file)
    engine.runAndWait()


def scene_to_sound_execute(scene_number):
    source_file = open("{2}animation/Scenes/{0}/{1}/{1}.txt".format(str(scene_number[0: 5]),
                                                                    scene_number, project_path), encoding="utf-8")
    lines = [line.rstrip() for line in source_file]
    sound_number = 0
    sound_count = ""
    speed = 1
    for line in lines:
        if line[0] == "@":
            char = line.replace("@", "")
            continue
        if line[0] == "№":
            speed = float(line.replace("№", ""))
            print(speed)
            continue
        sound_number += 1
        if sound_number < 100:
            sound_count = "0" + str(sound_number)
        if sound_number < 10:
            sound_count = "00" + str(sound_number)
        else:
            sound_count = sound_number

        sound_file = "{}_{}.wav".format(sound_count, char)
        export_dir = "{0}/animation/Scenes/{1}/{2}/export/audio/".format(project_path, scene_number[0: 5],
                                                                                          str(scene_number))
        if not os.path.isdir(export_dir):
            os.makedirs(export_dir)
        export_path = "{0}animation/Scenes/{1}/{2}/export/audio/{3}".format(project_path, scene_number[0: 5],
                                                                                             str(scene_number),
                                                                                             str(sound_file))
        print(export_path, line, speed)
        text_to_sound_pyttsx3(line, export_path, speed)
        speed = 1


