#!/usr/bin/env python3

import socket
import os
import platform
import psutil
from sys import platform as _platform


def host_parameters():
    global hdd_total, hdd_used
    print('Host name: ' + socket.gethostname())
    print('OS version: ' + platform.platform())
    print('CPU cores: ', os.cpu_count())
    # print('RAM in mb: ' + str(int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / 1024. ** 2)))
    print('RAM memory total mb:', int(psutil.virtual_memory()[0] / 1024. ** 2))
    if _platform == "linux" or platform == "linux2":
        hdd_total = int(psutil.disk_usage('/').total / 1024. ** 3)
        hdd_used = int(psutil.disk_usage('/').used / 1024. ** 3)
    elif platform == "win32":
        hdd_total = int(psutil.disk_usage('C:\\').total / 1024. ** 3)
        hdd_used = int(psutil.disk_usage('C:\\').used / 1024. ** 3)
    print('HDD size in gb: ', hdd_total)
    print('HDD disk usage in gb: ', hdd_used)


if __name__ == '__main__':
    host_parameters()
