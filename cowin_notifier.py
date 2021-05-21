#!/usr/bin/python
# coding: utf-8

import re
import subprocess
from shlex import join


def read_output(file_path='/tmp/output.tmp'):
    f_notify = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip('\n').strip() == '┌':
                notification = list()
            elif re.search(r'.\│.', line):
                notification.append(line[4:].strip('\n'))
            elif line.strip('\n').strip() == '└':
                f_notify.append(" ".join(notification))
    for n in f_notify:
        cmd = join(["osascript", "-e", 'display notification "{}" with title "{}"'.format(n.replace("'", ""), "Vaccine")])
        subprocess.run([cmd], shell=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    read_output()