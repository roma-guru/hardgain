#!/usr/bin/env python
import os
import sys


def print_logo():
    """
    Print's project's beautiful logo!
    """
    print("HARDGAIN Project")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    print_logo()
    execute_from_command_line(sys.argv)
