#!/usr/bin/python3
"""Module for the console (command interpreter).
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class for the console (command interpreter).
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered.
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Handles the end of file signal (Ctrl + D).
        """
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return

        new_instance = storage.CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name
        and id.
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    # Add other command methods as needed...

if __name__ == "__main__":
    HBNBCommand().cmdloop()

