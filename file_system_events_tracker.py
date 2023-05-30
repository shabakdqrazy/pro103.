import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/User/OneDrive/Desktop/yes"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")
    
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
    
    def on_moved(self, event):
        print(f"Moved: {event.src_path} to {event.dest_path}")
    
    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stoppedd!")
    observer.stop()
