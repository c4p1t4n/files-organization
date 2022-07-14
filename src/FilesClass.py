import json
from FileClass import File

class Files:
    def __init__(self):
       self.objects = []

    def append_objects_settings_in_list(self):
        with open('/home/c4p1/files-organization/utils/settings.json') as json_data:
            settings = json.load(json_data)
        for object in settings:
            object = settings[object]
            self.objects.append(File(object['extensions'],object['origin_directory'],object['destination_directory']))
    
    def move_files_in_objects(self):
        for object in self.objects:
            print('movie_files')
            object.movies_files()
