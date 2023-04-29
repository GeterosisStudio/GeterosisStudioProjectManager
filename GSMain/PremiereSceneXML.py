import xml.etree.ElementTree as ET
import json
import Log


project_path = None
episode_name = None
scene_name = None
between_name = None
xml_file = r"{0}animation\scenes\{1}\{2}\target\{3}.xml".format(project_path, episode_name, scene_name, between_name)
tree = ET.parse(xml_file)
root = tree.getroot()


def xml_to_dict(element):
    result = {}
    if element.attrib:
        result.update(element.attrib)
    if element.text:
        result['_text'] = element.text
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_result)
            else:
                result[child.tag] = [result[child.tag], child_result]
        else:
            result[child.tag] = child_result
    return result


my_dict = xml_to_dict(root)["sequence"]["media"]["video"]["track"]

with open(r'F:\bufer\test.json', 'w') as f:
    json.dump(xml_to_dict(root), f, indent=4)


def return_valid_tracks(full_list):
    valid_tracks = []
    for track in full_list:
        if "clipitem" in track:
            valid_tracks.append(track)
            for shot in track["clipitem"]:
                if shot["file"]["name"]['_text'] == "Graphic":
                    continue
                else:
                    break
    return valid_tracks


def dict_is_names(track):
    for shot in track["clipitem"]:
        if shot["file"]["name"]['_text'] == "Graphic":
            continue
        else:
            Log.info("This shot is not title:{}.".format(track["clipitem"].index(shot)))
            return False

    library = None
    with open(library) as f:
        source_char_variable_list = json.load(f)

    lib_char_names = []
    all_char_names = []
    valid_char_names = []
    invalid_char_names = []
    for i in source_char_variable_list["chars"]:
        lib_char_names.append(source_char_variable_list["chars"][i]["name"])

    for shot in track["clipitem"]:
        all_char_names.append(shot["file"]["filter"]["effect"]["name"]['_text'])

    for shot in track["clipitem"]:
        for i in range(len(lib_char_names)):
            if shot["file"]["filter"]["effect"]["name"]['_text'] in lib_char_names[i]:
                valid_char_names.append(shot["file"]["filter"]["effect"]["name"]['_text'])
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
        if shot["file"]["name"]['_text'] != "Graphic":
            pass
        else:
            return False
    return True


my_dict = return_valid_tracks(my_dict)

scene_name = my_dict[0]["clipitem"][0]["file"]['pathurl']['_text'].split("/")[-1]
source_start = int(my_dict[0]["clipitem"][0]["start"]['_text'])
source_end = int(my_dict[0]["clipitem"][0]["end"]['_text'])
target_start = int(my_dict[0]["clipitem"][0]["in"]['_text'])
target_end = int(my_dict[0]["clipitem"][0]["out"]['_text'])

# pprint.pprint(my_dict[0]["clipitem"][0]["start"]['_text'])
print(dict_is_names(my_dict[1]))
print(dict_is_shots(my_dict[0]))
