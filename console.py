#!/usr/bin/env python3
""" Import of all modules needed for the console"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City

""" creating a class HBNHcommand"""

class HBNBCommand(cmd.Cmd):
    """Command interpreter prompt."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

