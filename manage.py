#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    env = os.environ.get('DJANGO_ENV') or 'local'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(["devices.settings", env]))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
