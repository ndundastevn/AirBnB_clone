#!/usr/bin/python3
"""class HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Enty class for the cmd"""
    prompt = "(hbnb)"

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything """
        pass

    def do_EOF(self, line):
        """Signal to exit the programm"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
