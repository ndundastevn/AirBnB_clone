#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything """
        pass

    def do_greet(self, line):
        """Greet user"""
        if line:
            print("hello", line)
        else:
            print("hello")

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True
        
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
