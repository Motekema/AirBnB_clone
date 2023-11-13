#!/usr/bin/python3
"""Module for the console (command interpreter).
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User

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

    def do_all(self, line):
        """Prints all string representations of all instances based or not on the
        class name.
        """
        args = shlex.split(line)
        if not args:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in storage.CLASSES:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items() if class_name in key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
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

        del storage.all()[key]
        storage.save()

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        """
        commands = line.split('.')
        if len(commands) == 2:
            if commands[1] == "all()":
                self.do_all(commands[0])
            elif commands[1].startswith("count"):
                print(len([obj for obj in storage.all().values() if commands[0] in str(obj)]))
            elif commands[1].startswith("show"):
                id_str = commands[1].split('(')[1].split(')')[0]
                self.do_show("{} {}".format(commands[0], id_str))
            elif commands[1].startswith("destroy"):
                id_str = commands[1].split('(')[1].split(')')[0]
                self.do_destroy("{} {}".format(commands[0], id_str))
            elif commands[1].startswith("update"):
                update_str = commands[1].split('(')[1].split(')')[0]
                update_list = shlex.split(update_str.replace(',', ' '))
                if len(update_list) >= 3:
                    self.do_update("{} {}".format(commands[0], ' '.join(update_list)))
                else:
                    print("** attribute name missing **")
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == "__main__":
    HBNBCommand().cmdloop()

