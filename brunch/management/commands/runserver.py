import os
import subprocess

from django.contrib.staticfiles.management.commands.runserver import Command \
    as StaticfilesRunserverCommand

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

        brunch_args = settings.BRUNCH_CMD.split() + ["watch", "--stdin"]
        if settings.BRUNCH_SERVER:
            brunch_args.append('--server')
        self.stdout.write("Using {}".format(" ".join(brunch_args)))

        brunch_process = subprocess.Popen(brunch_args, cwd=settings.BRUNCH_DIR,
                                          stdin=subprocess.PIPE, stdout=self.stdout, stderr=self.stderr,)

        self.stdout.write('Brunch pid: {}'.format(brunch_process.pid))

        return brunch_process.pid
