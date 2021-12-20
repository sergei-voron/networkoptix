# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import os
import platform
import sysconfig

def host_parameters():
    # Use a breakpoint in the code line below to debug your script.
    print('Host name: ' + socket.gethostname())
    print('OS version: ' + platform.platform())
    print('CPU cores: ' + str(os.cpu_count()))
    print('RAM in kib: ' + str(int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')/1024)))
    print('HDD size: ' + socket.gethostname())
    print('HDD disk usage: ' + socket.gethostname())
    print('Host name: ' + socket.gethostname())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host_parameters()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
