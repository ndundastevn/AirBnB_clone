#!/usr/bin/python3
"""Entry point for the CLI"""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNB for the CLI"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Signal to exit the programm"""
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """create an instance"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Print the str rep of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                instance_id = args[1]
                key = class_name + '.' + instance_id
                if key in instances:
                    del instances[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print the str rep of all instances"""
        insts = storage.all()
        if not arg:
            print([str(instance) for instance in insts.values()])
        else:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(instance) for instance in insts.values()
                      if type(instance).__name__ == class_name])

    def do_update(self, arg):
        """Updates instances."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                instance_id = args[1]
                key = class_name + '.' + instance_id
                if key in instances:
                    instance = instances[key]
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        attr_name = args[2]
                        attr_value = args[3]
                        if hasattr(instance, attr_name):
                            attr_type = type(getattr(instance, attr_name))
                            setattr(instance, attr_name, attr_type(attr_value))
                            instance.save()
                            storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
