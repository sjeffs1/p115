import sys
import time
import random

import os
import shutil

# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

source = "C:/Users/Shlok/Downloads/main.txt"
dest = "C:/Users/Shlok/Downloads/newfile.txt"

os.rename(source, dest)