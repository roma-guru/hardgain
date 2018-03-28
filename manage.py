#!/usr/bin/env python
import os
import sys
import signal

def set_debug_trap(sig, frame):
    import ipdb
    ipdb.set_trace(frame)

def print_logo():
    """
    Print's project's beautiful logo!
    """
    print("HARDGAIN Project")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    signal.signal(signal.SIGTRAP, set_debug_trap)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    print_logo()
    execute_from_command_line(sys.argv)
