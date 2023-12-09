#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City

class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits the console"""
        return True

    def emptyline(self):
        """Overwriting the emptyline"""
        return False

    def do_quit(self, arg):
        """ To quit the program"""
        return True

    if __name__ == ' __main__':
        HBNBCommand().cmdloop()
