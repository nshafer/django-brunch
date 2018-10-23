import os
import subprocess
import sys

from django.contrib.staticfiles.management.commands.runserver import Command \
    as StaticfilesRunserverCommand
from django.utils import six

from brunch.conf import settings
from brunch.utils import check_pid


class Command(StaticfilesRunserverCommand):
    def run(self, **options):
        brunch_pid = os.environ.get('BRUNCH_PID')
        if not brunch_pid or not check_pid(int(brunch_pid)):
            os.environ['BRUNCH_PID'] = str(self.start_brunch())
        super(Command, self).run(**options)

    def start_brunch(self):
        self.stdout.write("Starting brunch in {}".format(settings.BRUNCH_DIR))

        cmd = settings.BRUNCH_CMD
        shell = settings.BRUNCH_SHELL

        args = ["watch", "--stdin"]
        if settings.BRUNCH_SERVER:
            args.append('--server')

        if isinstance(cmd, six.string_types):
            if shell:
                cmd = " ".join([cmd] + args)
            else:
                cmd = [cmd] + args
        elif not isinstance(cmd, list):
            cmd = list(cmd) + args
        else:
            cmd += args

        if shell and not isinstance(cmd, six.string_types):
            print("WARNING: BRUNCH_SHELL is true, but BRUNCH_CMD is not a string, attempting to fix")
            cmd = " ".join(cmd)

        self.stdout.write("Using {}{}".format("shell: " if shell else "", cmd if shell else " ".join(cmd)))

        brunch_process = subprocess.Popen(cmd, cwd=settings.BRUNCH_DIR, shell=settings.BRUNCH_SHELL,
                                          stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stderr)

        self.stdout.write('Brunch pid: {}'.format(brunch_process.pid))

        return brunch_process.pid
