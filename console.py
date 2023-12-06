#!/usr/bin/python3
import cmd


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
        return False

    if __name__ == ' __main__':
        HBNBCommand().cmdloop()
