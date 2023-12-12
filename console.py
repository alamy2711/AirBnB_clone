#!/usr/bin/python3
"""Coonsole module contains the entry point of the command interpreter."""
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def line_parser(line):
    """Parse a command line into a list of arguments."""
    args = []
    curly_braces_match = re.search(r"\{(.*?)\}", line)
    if curly_braces_match:
        args_dict_str = curly_braces_match.group()
        line = line.replace(args_dict_str, "temporary_text")

    for arg in shlex.split(line):
        args.append(arg.strip(","))

    if curly_braces_match:
        args[len(args) - 1] = args_dict_str

    return args


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter for interacting with HBNB models."""

    __classes_names = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Handle an empty line, does nothing."""
        pass

    do_EOF = do_quit

    def do_create(self, line):
        """
        Usage: create <class>.

        Create a new instance of a specified class.
        """
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
        """
        Usage: show <class> <id> or <class>.show(<id>)

        Show the string representation of an instance.
        """
        args = shlex.split(line)
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
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)

        Delete an instance based on the class name and id.
        """
        args = shlex.split(line)
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
        """
        Usage: all or all <class> or <class>.all()

        Prints all string representations of instances
        """
        args = shlex.split(line)
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

    def do_update(self, line):
        """
         Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)

         Updates an instance based on the class name and id by adding or
         updating attribute.
        """
        args = line_parser(line)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            try:
                if type(eval(args[2])) != dict:
                    raise NameError
                obj = objects[f"{args[0]}.{args[1]}"]
                args_dict = eval(args[2])
                for key, value in args_dict.items():
                    if hasattr(obj, key):
                        value_type = type(getattr(obj, key))
                        setattr(obj, key, value_type(value))
                    else:
                        setattr(obj, key, value)
                obj.save()
            except NameError:
                print("** value missing **")
        else:
            obj = objects[f"{args[0]}.{args[1]}"]
            if hasattr(obj, args[2]):
                value_type = type(getattr(obj, args[2]))
                setattr(obj, args[2], value_type(args[3]))
            else:
                setattr(obj, args[2], args[3])
            obj.save()

    def default(self, line):
        """Handle unknown commands."""
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
        }
        dot_match = re.search(r"\.", line)
        if dot_match:
            before_dot = line[: dot_match.span()[0]]
            after_dot = line[dot_match.span()[1]:]
            match = re.search(r"\((.*?)\)", after_dot)
            if match:
                method_name = after_dot[: match.span()[0]]
                method_args = match.group()[1:-1]
                if method_name in methods.keys():
                    new_line = f"{before_dot} {method_args}"
                    return methods[method_name](new_line)
        print(f"*** Unknown syntax: {line}")
        return False

    def do_count(self, line):
        """
        Usage: count <class> or <class>.count()

        Count the number of instances of a specified class.
        """
        args = shlex.split(line)
        objects = storage.all()
        count = 0
        for obj in objects.values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
