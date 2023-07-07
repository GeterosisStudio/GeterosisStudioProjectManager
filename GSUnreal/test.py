import unreal

def get_sequence_actors(sequence_path):
    level_sequence = unreal.load_asset(sequence_path)
    return level_sequence.get_bindings()

for actor in get_sequence_actors("/Script/LevelSequence.LevelSequence'/Game/ThirdPerson/Blueprints/NewLevelSequence.NewLevelSequence'"):
    if actor.get_object_class() ==
