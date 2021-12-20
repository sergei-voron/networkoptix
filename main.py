import socket
import os
import platform
import psutil
from sys import platform as _platform

def host_parameters():
    # Use a breakpoint in the code line below to debug your script.
    print('Host name: ' + socket.gethostname())
    print('OS version: ' + platform.platform())
    print('CPU cores: ' + str(os.cpu_count()))
    print('RAM in mb: ' + str(int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')/1024.**2)))
    if _platform == "linux" or platform == "linux2":
        hdd_total = str(int(psutil.disk_usage('/').total/1024.**3))
        hdd_used = str(int(psutil.disk_usage('/').used/1024.**3))
    elif platform == "win32":
        hdd_total = str(int(psutil.disk_usage('C:\\').total/1024.**3))
        hdd_used = str(int(psutil.disk_usage('C:\\').used/1024.**3))
    print('HDD size in gb: ' + hdd_total)
    print('HDD disk usage in gb: ' + hdd_used)
    print(_platform)


if __name__ == '__main__':
    host_parameters()
