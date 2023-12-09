#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    __classes_names = ["BaseModel"]
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    do_EOF = do_quit

    def do_create(self, line):
        if len(line.split()) == 1:
            try:
                new_instance = eval(line)()
                storage.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                objects = storage.all()
                obj_key = args[0] + "." + args[1]
                print(objects[obj_key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key not in objects.keys():
                print("** no instance found **")
            else:
                del objects[obj_key]
                storage.save()

    def do_all(self, line):
        args = line.split()
        objects = storage.all()
        str_list = []
        if len(args) > 0 and args[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if len(args) > 0 and obj.__class__.__name__ == args[0]:
                    str_list.append(str(obj))
                elif len(args) == 0:
                    str_list.append(str(obj))
            print(str_list)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
