#!/usr/bin/python3
"""
Contains the FileStorage class
"""


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
    instances
    Attributes:
        __file_path (str): private class attribute containing a file path
        __objects (dict): contains the id of all object instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__obects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): instance of a class Basemodel
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            n_dict = self.all()
            dict_serl = {}
            for key, value in n_dict.items():
                dict_serl[key] = value.to_dict()
            json.dump(dict_serl, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_objects = json.load(file)
            for key, vale in json_objects.items():
                class_name, obj_id = key.split('.')
                class_ = globals()[class_name]
                instance = class_(**value)
                self.__objects[key] = instance
