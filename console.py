#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone Project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is the command-line interface (CLI) for the AirBnB clone.
    It allows users to create and manage instances of different models.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on emptyline input"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
