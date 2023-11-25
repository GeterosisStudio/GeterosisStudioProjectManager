import xml.etree.ElementTree as ET
import json
import Log
import math

project_path = "E:/Projects/ILLUSION_1/"
episode_name = "e0010"
scene_name = "e0010s0030d0010v0030"
between_name = "Mom.xml"
xml_file = r"{0}animation/scenes/{1}/{2}/target/{3}".format(project_path, episode_name, scene_name, between_name)
tree = ET.parse(xml_file)
root = tree.getroot()


def xml_to_dict(element):
    result = {}
    if element.attrib:
        result.update(element.attrib)
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_result)
            else:
                result[child.tag] = [result[child.tag], child_result]
        else:
            result[child.tag] = child_result
    if result == {}:
        return element.text
    elif isinstance(result, dict) and len(result.keys()) == 1 and '_text' in result:
        return result['_text']
    else:
        return result


with open(r'F:\bufer\test.json', 'w') as f:
    json.dump(xml_to_dict(root), f, indent=4)


def return_valid_tracks(full_list):
    valid_tracks = []
    for track in full_list:
        if "clipitem" in track:
            valid_tracks.append(track)
            for shot in track["clipitem"]:
                if shot["file"]["name"] == "Graphic":
                    continue
                else:
                    break
    return valid_tracks


def dict_is_names(track):
    for shot in track["clipitem"]:
        if shot["file"]["name"] == "Graphic":
            continue
        else:
            Log.info("This shot is not title:{}.".format(track["clipitem"].index(shot)))
            return False

    library = r"C:\Users\AlexLip\Documents\GeterosisProjectManager\Settings\Libraries.json"
    with open(library) as f:
        source_char_variable_list = json.load(f)

    lib_char_names = []
    all_char_names = []
    valid_char_names = []
    invalid_char_names = []
    for i in source_char_variable_list["chars"]:
        lib_char_names.append(source_char_variable_list["chars"][i]["name"])

    for shot in track["clipitem"]:
        all_char_names.append(shot["file"]["filter"]["effect"]["name"])

    for shot in track["clipitem"]:
        for i in range(len(lib_char_names)):
            if shot["file"]["filter"]["effect"]["name"] in lib_char_names[i]:
                valid_char_names.append(shot["file"]["filter"]["effect"]["name"])
                break
        continue

    if range(len(all_char_names)) == range(len(valid_char_names)):
        return True

    else:
        for char_name in all_char_names:
            if char_name in valid_char_names:
                pass
            else:
                invalid_char_names.append(char_name)
        return Log.warning("This char name not defined:{}".format(invalid_char_names))


def dict_is_shots(dict):
    for shot in dict["clipitem"]:
        if shot["file"]["name"] != "Graphic":
            pass
        else:
            return False
    return True


my_dict = xml_to_dict(root)["sequence"]["media"]["video"]["track"]
my_dict = return_valid_tracks(my_dict)

target_frame_rate = float(xml_to_dict(root)["sequence"]["rate"]['timebase'])
count = 2
scene_name = my_dict[0]["clipitem"][count]["file"]['pathurl'].split("/")[-1]
source_frame_rate = float(my_dict[0]["clipitem"][count]["file"]['rate']['timebase'])
normal_frame_rate = float(target_frame_rate / source_frame_rate)
source_frame_speed = float(my_dict[0]["clipitem"][count]["filter"]["effect"]["parameter"][1]['value'])

source_start = int(math.ceil((int(my_dict[0]["clipitem"][count]["in"]) + 1) / normal_frame_rate))
source_end = int(math.ceil(float(my_dict[0]["clipitem"][count]["out"]) / normal_frame_rate) * source_frame_speed / 100)

target_start = int(my_dict[0]["clipitem"][count]["start"])
target_end = int(my_dict[0]["clipitem"][count]["end"])


source_frame_speed = float(my_dict[0]["clipitem"][count]["filter"]["effect"]["parameter"][1]['value'])
print(scene_name, source_start, source_end, target_start, target_end, source_frame_rate, target_frame_rate, source_frame_speed)