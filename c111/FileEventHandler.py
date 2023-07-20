import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ACER/Downloads"              
to_dir = "C:/Users/ACER/Downloads/test" 

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hey,{event.src_path}has been created")

    def on_deleted(self, event):
        print(f"oops,someone deleted{event.src_path}")
    
    def on_modified(self, event):
        print(f"hey,{event.src_path}has been modified")
    
    def on_moved(self, event):
        print(f"hey,{event.src_path}has been deleted")




try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    Observer.stop()

  
  



        













    
        
    